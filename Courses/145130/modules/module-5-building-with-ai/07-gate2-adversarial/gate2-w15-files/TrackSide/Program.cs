// Program.cs  .  TrackSide
//
// A console front end for the cross country coach. It reads practice notes
// from a JSON file and asks the model service to summarize and classify each
// one. The model runs locally and the service wraps it, so this program never
// reads a raw model answer.
//
//   dotnet run --project TrackSide -- review
//   dotnet run --project TrackSide -- review --file practice_notes.json
//   dotnet run --project TrackSide -- health
//
// Exit codes: 0 finished, 1 the service could not be used, 2 wrong usage.

using System.Net;
using System.Net.Http;
using System.Net.Http.Headers;
using System.Net.Sockets;
using System.Text;
using System.Text.Json;
using System.Text.Json.Serialization;

namespace TrackSide;

/// <summary>Where the service says an answer came from.</summary>
public static class ResultSource
{
    public const string Model = "model";
    public const string Fallback = "fallback";
    public const string None = "none";
}

/// <summary>What the service reports when something went wrong.</summary>
public sealed class ServiceError
{
    [JsonPropertyName("kind")]
    public string? Kind { get; set; }

    [JsonPropertyName("message")]
    public string? Message { get; set; }
}

/// <summary>The one response shape POST /generate ever returns.</summary>
public sealed class GenerateResponse
{
    [JsonPropertyName("ok")]
    public bool Ok { get; set; }

    [JsonPropertyName("task")]
    public string? Task { get; set; }

    [JsonPropertyName("result")]
    public JsonElement Result { get; set; }

    [JsonPropertyName("source")]
    public string? Source { get; set; }

    [JsonPropertyName("elapsed_ms")]
    public int ElapsedMs { get; set; }

    [JsonPropertyName("error")]
    public ServiceError? Error { get; set; }

    public bool HasResult => Result.ValueKind == JsonValueKind.Object;

    /// <summary>The reason this body is not the envelope, or null when it is.</summary>
    public string? Problem()
    {
        if (string.IsNullOrWhiteSpace(Source))
        {
            return "the response has no source field";
        }

        if (string.IsNullOrWhiteSpace(Task))
        {
            return "the response has no task field";
        }

        if (Ok && !HasResult)
        {
            return "the response says ok, but carries no result object";
        }

        return null;
    }
}

public sealed class SummaryResult
{
    [JsonPropertyName("summary")]
    public string Summary { get; set; } = string.Empty;

    [JsonPropertyName("bullets")]
    public List<string> Bullets { get; set; } = new();
}

public sealed class ClassificationResult
{
    [JsonPropertyName("label")]
    public string Label { get; set; } = string.Empty;

    [JsonPropertyName("confidence_note")]
    public string ConfidenceNote { get; set; } = string.Empty;
}

public sealed class HealthReport
{
    [JsonPropertyName("service")]
    public string? Service { get; set; }

    [JsonPropertyName("status")]
    public string? Status { get; set; }

    [JsonPropertyName("model_reachable")]
    public bool ModelReachable { get; set; }

    [JsonPropertyName("timeout_seconds")]
    public double TimeoutSeconds { get; set; }

    [JsonPropertyName("retries")]
    public int Retries { get; set; }
}

public sealed class PracticeNote
{
    [JsonPropertyName("id")]
    public string Id { get; set; } = string.Empty;

    [JsonPropertyName("written_by")]
    public string WrittenBy { get; set; } = string.Empty;

    [JsonPropertyName("text")]
    public string Text { get; set; } = string.Empty;
}

public enum FailureKind
{
    None,
    ServiceDown,
    Timeout,
    HttpError,
    MalformedPayload,
    RequestRejected,
}

public sealed record Failure(FailureKind Kind, string Message, string WhatToDo);

public static class Program
{
    // Where the model service listens. Change this line if it moves.
    private const string ServiceUrl = "http://127.0.0.1:5157";

    // Sent with every request so the service knows this program is allowed
    // to use it.
    private const string SharedToken = "mcctc-lab-shared-2026-trackside";

    // Long enough for the service to finish its own retry before we give up.
    private static readonly TimeSpan RequestTimeout = TimeSpan.FromSeconds(5);

    private static readonly JsonSerializerOptions JsonOptions = new()
    {
        PropertyNameCaseInsensitive = true,
        WriteIndented = false,
    };

    private static readonly string[] Tasks = { "summarize", "classify" };

    public static async Task<int> Main(string[] args)
    {
        if (args.Length == 0)
        {
            Console.WriteLine("TrackSide . review the coach's practice notes");
            Console.WriteLine();
            Console.WriteLine("  health                    is the service up");
            Console.WriteLine("  review [--file <path>]    summarize and classify every note");
            return 2;
        }

        string command = args[0].ToLowerInvariant();
        string file = ValueAfter(args, "--file") ?? "practice_notes.json";

        Console.WriteLine($"TrackSide . service {ServiceUrl}");

        if (command == "health")
        {
            return await RunHealth().ConfigureAwait(false);
        }

        if (command == "review")
        {
            return await RunReview(file).ConfigureAwait(false);
        }

        Console.Error.WriteLine($"Unknown command '{command}'.");
        return 2;
    }

    private static async Task<int> RunHealth()
    {
        using HttpClient http = BuildClient();
        (HealthReport? report, Failure? failure) = await GetAsync<HealthReport>(http, "health")
            .ConfigureAwait(false);
        if (failure is not null)
        {
            ReportFailure(failure);
            return 1;
        }

        Console.WriteLine($"  service          {report!.Service}, status {report.Status}");
        Console.WriteLine($"  model reachable  {(report.ModelReachable ? "yes" : "no")}");
        Console.WriteLine($"  service waits    {report.TimeoutSeconds:0.#} s per model call, {report.Retries} retry");
        return 0;
    }

    private static async Task<int> RunReview(string file)
    {
        List<PracticeNote>? notes = ReadNotes(file);
        if (notes is null)
        {
            return 2;
        }

        Console.WriteLine($"Reviewing {notes.Count} practice notes from {file}");

        foreach (PracticeNote note in notes)
        {
            Console.WriteLine();
            Console.WriteLine($"== {note.Id} from {note.WrittenBy} ==");

            string text = ValidateNote(note.Text);
            Console.WriteLine($"  \"{Shorten(text, 84)}\"");

            // A fresh client for each note keeps one slow note from holding
            // up the next one.
            using HttpClient http = BuildClient();

            foreach (string task in Tasks)
            {
                (GenerateResponse? envelope, Failure? failure) =
                    await GenerateAsync(http, task, text).ConfigureAwait(false);
                if (failure is not null)
                {
                    ReportFailure(failure);
                    if (failure.Kind == FailureKind.ServiceDown)
                    {
                        return 1;
                    }

                    continue;
                }

                PrintAnswer(envelope!);
            }
        }

        return 0;
    }

    /// <summary>
    /// Trims the coach's note and rejects one that is empty, so the service
    /// is never asked about a note with nothing in it.
    /// </summary>
    private static string ValidateNote(string text)
    {
        return text.Trim();
    }

    private static void PrintAnswer(GenerateResponse envelope)
    {
        Console.WriteLine($"  [{envelope.Task}] answered in {envelope.ElapsedMs} ms");

        if (envelope.Task == "summarize" && envelope.HasResult)
        {
            SummaryResult? summary = envelope.Result.Deserialize<SummaryResult>(JsonOptions);
            if (summary is not null)
            {
                Console.WriteLine($"  summary: {summary.Summary}");
                foreach (string bullet in summary.Bullets)
                {
                    Console.WriteLine($"    - {bullet}");
                }
            }

            return;
        }

        if (envelope.Task == "classify" && envelope.HasResult)
        {
            ClassificationResult? classification =
                envelope.Result.Deserialize<ClassificationResult>(JsonOptions);
            if (classification is not null)
            {
                Console.WriteLine($"  label: {classification.Label}");
                Console.WriteLine($"  note:  {classification.ConfidenceNote}");
            }

            return;
        }

        Console.WriteLine("  the result could not be read");
    }

    private static HttpClient BuildClient()
    {
        HttpClient http = new()
        {
            BaseAddress = new Uri(ServiceUrl.TrimEnd('/') + "/"),
            Timeout = RequestTimeout,
        };
        http.DefaultRequestHeaders.Accept.Add(new MediaTypeWithQualityHeaderValue("application/json"));
        http.DefaultRequestHeaders.Add("X-TrackSide-Token", SharedToken);
        return http;
    }

    private static async Task<(TValue? Value, Failure? Failure)> GetAsync<TValue>(
        HttpClient http, string path) where TValue : class
    {
        try
        {
            using HttpResponseMessage response = await http.GetAsync(path).ConfigureAwait(false);
            string text = await response.Content.ReadAsStringAsync().ConfigureAwait(false);
            return ReadBody<TValue>(response.StatusCode, text, value => null);
        }
        catch (TaskCanceledException)
        {
            return (null, TimeoutFailure());
        }
        catch (HttpRequestException error)
        {
            return (null, ConnectionFailure(error));
        }
    }

    private static async Task<(GenerateResponse? Value, Failure? Failure)> GenerateAsync(
        HttpClient http, string task, string prompt)
    {
        string body = JsonSerializer.Serialize(new Dictionary<string, string>
        {
            ["task"] = task,
            ["prompt"] = prompt,
        });

        for (int attempt = 1; attempt <= 2; attempt++)
        {
            try
            {
                using StringContent content = new(body, Encoding.UTF8, "application/json");
                using HttpResponseMessage response =
                    await http.PostAsync("generate", content).ConfigureAwait(false);
                string text = await response.Content.ReadAsStringAsync().ConfigureAwait(false);
                return ReadBody<GenerateResponse>(response.StatusCode, text,
                                                  envelope => envelope.Problem());
            }
            catch (TaskCanceledException)
            {
                // A timeout might be a blip between here and the service, so
                // one more try is worth the wait.
                if (attempt == 2)
                {
                    return (null, TimeoutFailure());
                }
            }
            catch (HttpRequestException error)
            {
                return (null, ConnectionFailure(error));
            }
        }

        return (null, TimeoutFailure());
    }

    private static (TValue? Value, Failure? Failure) ReadBody<TValue>(
        HttpStatusCode status, string text, Func<TValue, string?> check) where TValue : class
    {
        TValue? value;
        try
        {
            value = JsonSerializer.Deserialize<TValue>(text, JsonOptions);
        }
        catch (JsonException error)
        {
            return (null, MalformedFailure(status, text, error.Message));
        }

        if (value is null)
        {
            return (null, MalformedFailure(status, text, "the body was JSON null"));
        }

        string? problem = check(value);
        if (problem is not null)
        {
            return (null, MalformedFailure(status, text, problem));
        }

        if (status == HttpStatusCode.OK)
        {
            return (value, null);
        }

        if (value is GenerateResponse envelope && !envelope.Ok && envelope.Error is not null)
        {
            return (null, new Failure(
                FailureKind.RequestRejected,
                $"the service refused the request ({envelope.Error.Kind}): {envelope.Error.Message}",
                "Fix the request and send it again. Nothing was asked of the model."));
        }

        return (null, new Failure(
            FailureKind.HttpError,
            $"the service answered with HTTP {(int)status}.",
            "Check the service console for the matching line, then try again."));
    }

    private static Failure TimeoutFailure() => new(
        FailureKind.Timeout,
        $"the service at {ServiceUrl} did not answer within {RequestTimeout.TotalSeconds:0.#} seconds.",
        "The model may still be loading. Try again in a minute.");

    private static Failure ConnectionFailure(HttpRequestException error)
    {
        if (error.InnerException is SocketException socket &&
            socket.SocketErrorCode == SocketError.ConnectionRefused)
        {
            return new Failure(
                FailureKind.ServiceDown,
                $"nothing is listening at {ServiceUrl}.",
                "Start the service with: python practice_service.py, then run this again.");
        }

        return new Failure(
            FailureKind.ServiceDown,
            $"the connection to {ServiceUrl} failed ({error.Message})",
            "Check that the service is running on that machine.");
    }

    private static Failure MalformedFailure(HttpStatusCode status, string text, string problem)
        => new(
            FailureKind.MalformedPayload,
            $"the reply to HTTP {(int)status} was not the response this program expects: {problem}",
            $"Confirm {ServiceUrl} is the model service and not another program. First 120 characters received: {Shorten(text, 120)}");

    private static void ReportFailure(Failure failure)
    {
        Console.Error.WriteLine();
        Console.Error.WriteLine($"  {Heading(failure.Kind)}");
        Console.Error.WriteLine($"  {failure.Message}");
        Console.Error.WriteLine($"  {failure.WhatToDo}");
    }

    private static string Heading(FailureKind kind) => kind switch
    {
        FailureKind.ServiceDown => "The model service is not answering.",
        FailureKind.Timeout => "The model service took too long.",
        FailureKind.HttpError => "The model service returned an error status.",
        FailureKind.MalformedPayload => "The reply was not the shape this program expects.",
        FailureKind.RequestRejected => "The model service refused this request.",
        _ => "Something went wrong.",
    };

    private static List<PracticeNote>? ReadNotes(string path)
    {
        string full = Path.GetFullPath(path);
        if (!File.Exists(full))
        {
            Console.Error.WriteLine($"No file at {full}.");
            return null;
        }

        try
        {
            return JsonSerializer.Deserialize<List<PracticeNote>>(File.ReadAllText(full), JsonOptions);
        }
        catch (JsonException error)
        {
            Console.Error.WriteLine($"{full} is not valid JSON: {error.Message}");
            return null;
        }
    }

    private static string? ValueAfter(string[] args, string flag)
    {
        for (int index = 0; index < args.Length - 1; index++)
        {
            if (string.Equals(args[index], flag, StringComparison.OrdinalIgnoreCase))
            {
                return args[index + 1];
            }
        }

        return null;
    }

    private static string Shorten(string text, int limit)
    {
        string flattened = text.Replace("\r", " ").Replace("\n", " ").Trim();
        return flattened.Length <= limit ? flattened : flattened.Substring(0, limit) + "...";
    }
}
