# User Help

## What this program does

The headline service is a CLI-adjacent microservice that leverages an LLM to
perform abstractive headline generation on arbitrary text payloads via a
RESTful interface.

## How to start it

Install the model runtime with administrator rights on your own laptop, pull the
model, then export the environment variables and start the service. If you are
technical this takes about five minutes. Full instructions are in the repository
README for developers.

## What every message means

Error messages are printed to stderr with a description of the problem. Check
the service logs for more detail, and consult the error kind table in the I/O
specification for the meaning of each kind.

## When it says the answer is a fallback

The fallback is used when the model is unavailable.
