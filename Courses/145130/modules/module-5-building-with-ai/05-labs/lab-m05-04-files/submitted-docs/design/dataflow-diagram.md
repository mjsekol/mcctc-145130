# Dataflow

## The layers

```
User -> client -> headline service (Flask) -> local model
```

Three layers. The client handles presentation, the Flask service handles
business logic, and the model does the language work. Each layer talks only to
the one below it.

## One request step by step

1. The user types a command.
2. The client sends the request to the service.
3. The service calls the model at `/api/headline`.
4. The model returns JSON.
5. The service returns the JSON to the client.
6. The client prints it.

## Trust boundaries

The service validates all input before use.
