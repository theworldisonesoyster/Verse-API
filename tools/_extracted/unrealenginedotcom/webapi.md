- UnrealEngine.com
- WebAPI

## Classes and Structs
| Name | Description |
| client_id | Verse path: /UnrealEngine.com/WebAPI Usage: Licensed users create a derived version of client_id in their module. The Verse class path for your derived client_id is then used as the configuration key in your backend service to map to your endpoint. WARNING: do not make your derived client_id class public. This object type is your private key to your backend. Example: my_client_id := class(client_id) MyClient := MakeClient(my_client_id) |
| client |  |
| response |  |
| body_response |  |

## Functions
| Name | Description |
| MakeClient |  |
