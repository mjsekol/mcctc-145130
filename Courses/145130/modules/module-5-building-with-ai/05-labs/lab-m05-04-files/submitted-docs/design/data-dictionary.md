# Data Dictionary

## Every field

| Field | Type |
|---|---|
| ok | boolean |
| result | object |
| source | string |
| elapsed_ms | integer |
| error | object |
| headline | string |
| confidence | float |

## Where each field comes from

All fields come from the service. The service builds them from the model
response. The client reads them.

## What happens when a field is wrong

The service handles it.
