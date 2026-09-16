# I/O Specification

## The service

`headline-service` listens on port 5157 and exposes `/health`, `/generate`,
`/api/headline`, and `/api/summary`. Authentication uses a bearer token set in
the environment.

## The request

```json
{"task": "headline", "prompt": "some text"}
```

The prompt may be any length. The service will truncate it if needed so the
caller never has to worry about limits.

## The response envelope

```json
{"ok": true, "result": {}, "source": "model", "elapsed_ms": 12, "error": null}
```

When `ok` is false, the model failed. When `ok` is true, the model succeeded.
This makes error handling straightforward for the caller: check `ok` and you are
done.

## Result shapes

The `headline` task returns a `headline` string of up to 500 characters and a
`confidence` number between 0 and 1.

## Error kinds

Errors are returned in the `error` field with a `kind` and a `message`. The
service retries failed model calls up to 5 times with exponential backoff before
giving up, so most transient errors never reach the caller at all.
