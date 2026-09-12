Verse path: /UnrealEngine.com Module import path: /UnrealEngine.com/ControlInput
- UnrealEngine.com
- ControlInput

## Classes and Structs
| Name | Description |
| input_events(t) | Input_events is a container for user input events which can be subscribed to. Use the 'GetPlayerInput' and 'GetInputEvents' functions to retrieve an input_events object for a given player. Low-level notifications of current user input: DetectionBeginEvent, DetectionOngoingEvent, and DetectionEndEvent. High-level notifications of triggered events: ActivationTriggeredEvent and ActivationCanceledEvent. /—----------<-------\ DetectionBeginEvent -> DetectionOngoingEvent -> ActivationTriggeredEvent -> DetectionEndEvent /\ /\ / ---------------------> ActivationCanceledEvent ----------------------/ |
| player_input | This is the main manager class for input-related settings and functions for a player. |

## Functions
| Name | Description |
| input_events | Input_events is a container for user input events which can be subscribed to. Use the 'GetPlayerInput' and 'GetInputEvents' functions to retrieve an input_events object for a given player. Low-level notifications of current user input: DetectionBeginEvent, DetectionOngoingEvent, and DetectionEndEvent. High-level notifications of triggered events: ActivationTriggeredEvent and ActivationCanceledEvent. /—----------<-------\ DetectionBeginEvent -> DetectionOngoingEvent -> ActivationTriggeredEvent -> DetectionEndEvent /\ /\ / ---------------------> ActivationCanceledEvent ----------------------/ |
| GetPlayerInput | Access input-related data and settings for a player. |
