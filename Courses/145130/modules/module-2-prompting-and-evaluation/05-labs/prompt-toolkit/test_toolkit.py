# test_toolkit.py  ·  145130 Module 2 prompt toolkit
#
# Runs the stub, ask.py, and compare_runs.py against each other and checks the
# behaviour every lab in this module depends on.
#
# Run it:
#   python test_toolkit.py
#
# It starts its own stub on a free port, so nothing needs to be running first.

import io
import json
import pathlib
import sys
import tempfile
import unittest
from contextlib import redirect_stdout

sys.path.insert(0, str(pathlib.Path(__file__).parent))

import ask
import compare_runs
import stub_model_server as stub


class StubCase(unittest.TestCase):
    """Base class that gives each test its own stub and its own runs folder."""

    mode = stub.SUCCESS
    delay = 30.0

    def setUp(self):
        self.server = stub.start_in_background(mode=self.mode, delay_seconds=self.delay)
        self.endpoint = self.server.base_url
        self.temp = tempfile.TemporaryDirectory()
        self.runs = pathlib.Path(self.temp.name) / "runs"

    def tearDown(self):
        self.server.shutdown()
        self.server.server_close()
        self.temp.cleanup()

    def run_ask(self, prompt, label="t"):
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            code = ask.main(["--prompt", prompt, "--label", label,
                             "--runs-dir", str(self.runs),
                             "--endpoint", self.endpoint, "--timeout", "5"])
        return code, buffer.getvalue()


class PromptElementsChangeTheReply(StubCase):

    def test_role_line_changes_the_opening(self):
        text, _ = stub.compose_reply("Write a study plan for a unit exam.")
        with_role, _ = stub.compose_reply(
            "You are a veteran study skills teacher. Write a study plan for a unit exam.")
        self.assertNotEqual(text, with_role)
        self.assertTrue(with_role.startswith("As a veteran study skills teacher"))

    def test_format_instruction_changes_the_shape(self):
        prose, _ = stub.compose_reply("Explain the Friday equipment checkout.")
        numbered, _ = stub.compose_reply(
            "Explain the Friday equipment checkout. Use a numbered list.")
        as_json, _ = stub.compose_reply(
            "Explain the Friday equipment checkout. Return only JSON, no other text, "
            "with keys subject, steps.")
        self.assertEqual(compare_runs.shape_of(prose), "prose")
        self.assertEqual(compare_runs.shape_of(numbered), "numbered")
        self.assertEqual(compare_runs.shape_of(as_json), "json")
        self.assertTrue(compare_runs.parses_as_json(as_json))
        self.assertEqual(sorted(json.loads(as_json)), ["steps", "subject"])

    def test_json_without_only_arrives_wrapped_in_prose(self):
        """The Thursday lesson, in one assertion. 'Return JSON' is not enough."""
        wrapped, _ = stub.compose_reply(
            "Explain the Friday equipment checkout. Return JSON with keys subject, steps.")
        self.assertFalse(compare_runs.parses_as_json(wrapped))
        self.assertIn("{", wrapped)
        self.assertTrue(wrapped.startswith("Here are some thoughts"))

    def test_a_topic_word_is_not_a_format_instruction(self):
        """'hash table' is a topic. 'as a table' is a format. Tell them apart."""
        topic, _ = stub.compose_reply(
            "Write a study plan for how a hash table handles a collision. "
            "Give me 4 steps in a numbered list.")
        self.assertEqual(compare_runs.shape_of(topic), "numbered")
        wanted, _ = stub.compose_reply(
            "Explain the Friday equipment checkout as a table.")
        self.assertEqual(compare_runs.shape_of(wanted), "table")

    def test_step_count_is_obeyed(self):
        text, _ = stub.compose_reply("Give me 3 steps for the Friday equipment checkout.")
        self.assertEqual(len(compare_runs.NUMBERED_ITEM.findall(text)), 3)

    def test_word_cap_shortens_the_reply(self):
        long_reply, _ = stub.compose_reply("Explain a study plan for a unit exam.")
        short_reply, _ = stub.compose_reply(
            "Explain a study plan for a unit exam. Keep it under 25 words.")
        self.assertLess(len(short_reply.split()), len(long_reply.split()))
        self.assertLessEqual(len(short_reply.split()), 25)

    def test_no_constraints_produces_hedging(self):
        loose, _ = stub.compose_reply("Tell me about a study plan for a unit exam.")
        tight, _ = stub.compose_reply(
            "You are a study skills teacher. Give me 4 steps for a study plan "
            "for a unit exam, under 60 words.")
        self.assertGreater(compare_runs.measure({"response": loose})["hedges"],
                           compare_runs.measure({"response": tight})["hedges"])

    def test_audience_instruction_appears(self):
        text, _ = stub.compose_reply(
            "You are a librarian. Explain the Friday equipment checkout for a ninth grader.")
        self.assertIn("ninth grader", text)


class CitationBehaviour(StubCase):

    def test_asking_for_sources_with_none_supplied_invents_three(self):
        text, parsed = stub.compose_reply(
            "Write a research brief on retrieval practice. Cite your sources.")
        self.assertTrue(parsed["wants_sources"])
        self.assertFalse(parsed["grounded"])
        self.assertEqual(len(compare_runs.SOURCE_ITEM.findall(text)), 3)

    def test_the_same_prompt_invents_the_same_three(self):
        prompt = "Write a research brief on retrieval practice. Cite your sources."
        first, _ = stub.compose_reply(prompt)
        second, _ = stub.compose_reply(prompt)
        self.assertEqual(first, second)

    def test_different_prompts_invent_different_sources(self):
        a, _ = stub.compose_reply("Write a research brief on checkout procedures. Cite sources.")
        b, _ = stub.compose_reply("Write a research brief on revision windows. Cite sources.")
        self.assertNotEqual(
            compare_runs.SOURCE_ITEM.findall(a), compare_runs.SOURCE_ITEM.findall(b))

    def test_grounding_stops_the_invention(self):
        prompt = ("Answer the question using only the sources below. "
                  "If the answer is not in the sources, say I do not know.\n"
                  "SOURCE: Student handbook, section 4, equipment checkout\n"
                  "SOURCE: Club bylaws, article 2\n"
                  "Question: who signs out a tripod? Cite your sources.")
        text, parsed = stub.compose_reply(prompt)
        self.assertTrue(parsed["grounded"])
        self.assertEqual(len(parsed["provided_sources"]), 2)
        self.assertIn("Student handbook", text)
        for invented in stub.FAKE_VENUES:
            self.assertNotIn(invented, text)

    def test_grounded_and_allowed_to_refuse_produces_a_refusal(self):
        prompt = ("Use only the sources below. If it is not in the sources, "
                  "say I do not know. Cite your sources.\n"
                  "Question: what is the repair budget?")
        text, _ = stub.compose_reply(prompt)
        self.assertIn("I do not know", text)


class HappyPath(StubCase):

    def test_ask_records_a_run(self):
        code, output = self.run_ask("Give me 4 steps for the Friday equipment checkout.", "v1")
        self.assertEqual(code, ask.EXIT_OK)
        run = json.loads((self.runs / "v1.json").read_text(encoding="utf-8"))
        self.assertEqual(run["label"], "v1")
        self.assertGreater(run["response_words"], 0)
        self.assertIn("recorded in", output)

    def test_run_log_gains_a_row_per_run(self):
        self.run_ask("Explain the Friday equipment checkout.", "a")
        self.run_ask("Explain the Friday equipment checkout in bullets.", "b")
        log = (self.runs / "run_log.md").read_text(encoding="utf-8")
        self.assertEqual(log.count("\n| a |"), 1)
        self.assertEqual(log.count("\n| b |"), 1)

    def test_no_clock_date_is_written_into_a_run_file(self):
        self.run_ask("Explain the Friday equipment checkout.", "a")
        run = json.loads((self.runs / "a.json").read_text(encoding="utf-8"))
        self.assertNotIn("created_at", run)
        self.assertNotIn("timestamp", run)

    def test_empty_prompt_is_refused_before_any_request(self):
        code, output = self.run_ask("   ", "blank")
        self.assertEqual(code, ask.EXIT_UNUSABLE)
        self.assertIn("empty prompt", output)
        self.assertEqual(self.server.generate_calls, 0)

    def test_compare_runs_prints_one_row_per_run(self):
        self.run_ask("Explain the Friday equipment checkout.", "prose")
        self.run_ask("Explain the Friday equipment checkout. Use a numbered list.", "numbered")
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            code = compare_runs.main([str(self.runs)])
        output = buffer.getvalue()
        self.assertEqual(code, 0)
        self.assertIn("| prose |", output)
        self.assertIn("| numbered |", output)
        self.assertIn("2 run(s) compared", output)


class FailuresAreToldApart(StubCase):

    def test_unreachable_endpoint(self):
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            code = ask.main(["--prompt", "hello", "--label", "x",
                             "--runs-dir", str(self.runs),
                             "--endpoint", "http://127.0.0.1:1", "--timeout", "3"])
        self.assertEqual(code, ask.EXIT_UNREACHABLE)
        self.assertIn("nothing is listening", buffer.getvalue())

    def test_http_error(self):
        self.server.mode = stub.ERROR
        code, output = self.run_ask("hello", "x")
        self.assertEqual(code, ask.EXIT_HTTP_ERROR)
        self.assertIn("HTTP 500", output)

    def test_malformed_json(self):
        self.server.mode = stub.MALFORMED
        code, output = self.run_ask("hello", "x")
        self.assertEqual(code, ask.EXIT_MALFORMED)
        self.assertIn("not valid JSON", output)

    def test_missing_response_field(self):
        self.server.mode = stub.MISSING_RESPONSE
        code, output = self.run_ask("hello", "x")
        self.assertEqual(code, ask.EXIT_UNUSABLE)
        self.assertIn("no 'response' field", output)

    def test_not_done(self):
        self.server.mode = stub.NOT_DONE
        code, output = self.run_ask("hello", "x")
        self.assertEqual(code, ask.EXIT_UNUSABLE)
        self.assertIn("not marked done", output)

    def test_empty_response(self):
        self.server.mode = stub.EMPTY_RESPONSE
        code, output = self.run_ask("hello", "x")
        self.assertEqual(code, ask.EXIT_UNUSABLE)
        self.assertIn("empty", output)

    def test_nothing_is_recorded_when_a_run_fails(self):
        self.server.mode = stub.ERROR
        self.run_ask("hello", "x")
        self.assertFalse((self.runs / "x.json").exists())


class SlowServer(StubCase):
    mode = stub.SLOW
    delay = 6.0

    def test_timeout_is_its_own_failure(self):
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            code = ask.main(["--prompt", "hello", "--label", "x",
                             "--runs-dir", str(self.runs),
                             "--endpoint", self.endpoint, "--timeout", "1"])
        self.assertEqual(code, ask.EXIT_TIMEOUT)
        self.assertIn("no answer inside", buffer.getvalue())


class RateLimited(StubCase):
    mode = stub.RATE_LIMITED

    def test_retry_after_is_respected_then_the_run_gives_up(self):
        original = ask.time.sleep
        waits = []
        ask.time.sleep = lambda seconds: waits.append(seconds)
        try:
            code, output = self.run_ask("hello", "x")
        finally:
            ask.time.sleep = original
        self.assertEqual(code, ask.EXIT_HTTP_ERROR)
        self.assertIn("HTTP 429", output)
        self.assertEqual(waits, [stub.RETRY_AFTER_SECONDS] * ask.MAX_RATE_LIMIT_RETRIES)


class ServerShape(StubCase):

    def test_generate_rejects_a_streaming_request(self):
        import urllib.request
        import urllib.error
        body = json.dumps({"model": "m", "prompt": "hi"}).encode("utf-8")
        request = urllib.request.Request(self.endpoint + "/api/generate", data=body,
                                         headers={"Content-Type": "application/json"})
        with self.assertRaises(urllib.error.HTTPError) as caught:
            urllib.request.urlopen(request, timeout=5)
        self.assertEqual(caught.exception.code, 400)

    def test_stats_counts_calls(self):
        self.run_ask("Explain the Friday equipment checkout.", "a")
        self.run_ask("Explain the Friday equipment checkout.", "b")
        self.assertEqual(self.server.generate_calls, 2)

    def test_parse_endpoint_reports_detected_elements(self):
        import urllib.parse
        import urllib.request
        query = urllib.parse.urlencode(
            {"prompt": "You are a librarian. Give me 3 steps in a numbered list, under 40 words."})
        with urllib.request.urlopen(f"{self.endpoint}/stub/parse?{query}", timeout=5) as response:
            parsed = json.loads(response.read().decode("utf-8"))
        self.assertEqual(parsed["role"], "librarian")
        self.assertEqual(parsed["format"], "numbered")
        self.assertEqual(parsed["step_count"], 3)
        self.assertEqual(parsed["word_cap"], 40)


if __name__ == "__main__":
    unittest.main(verbosity=2)
