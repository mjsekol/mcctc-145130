# IPO Chart

## Input

The user provides a request as a string. The system also reads configuration
from environment variables and from `config.json` in the project root.

## Process

The request is validated, sent to the model, and the response is parsed into a
structured result. Results are cached for 10 minutes so that repeated requests
are fast.

## Output

A JSON response containing the result, along with a status code. The client
displays the headline to the user.
