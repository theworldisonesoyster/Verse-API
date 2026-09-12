Input_events is a container for user input events which can be subscribed to.
- Use the 'GetPlayerInput' and 'GetInputEvents' functions to retrieve an input_events object for a given player.
- Low-level notifications of current user input: DetectionBeginEvent, DetectionOngoingEvent, and DetectionEndEvent.
- High-level notifications of triggered events: ActivationTriggeredEvent and ActivationCanceledEvent. /—----------<-------\ DetectionBeginEvent -> DetectionOngoingEvent -> ActivationTriggeredEvent -> DetectionEndEvent /\ /\ / ---------------------> ActivationCanceledEvent ----------------------/
|  |  |
| Verse using statement | using { /UnrealEngine.com/ControlInput } |
input_events<public>(t:any):input_events(t)
This function is a parametric type, meaning it returns a class or interface rather than a value or object instance.

## Parameters
input_events takes the following parameters:
| Name | Type | Description |
| t | any |  |

### Generated Class
input_events returns the parametric class input_events(t).

_（Attributes/Specifiers/Effects 公共说明见《Specifiers 与 Effects 对照》，此处不重复官网公共表格）_
