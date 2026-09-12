Module import path: /Verse.org/Input
- Verse.org
- Input Gameplay
- UI

## Classes and Structs
| Name | Description |
| available_input_devices | Flags for input devices currently available to the player. Updates at runtime as devices connect or disconnect. Note that Keyboard and Mouse always carry the same value because the engine groups them as a single capability today. |
| input_events(t) | Input_events is a container for user input events which can be subscribed to. Use the 'GetPlayerInput' and 'GetInputEvents' functions to retrieve an input_events object for a given player. Low-level notifications of current user input: BeginDetectEvent, DetectionOngoingEvent, and EndDetectEvent. High-level notifications of triggered events: TriggerActivationEvent and CancelActivationEvent. /—----------<-------\ BeginDetectEvent -> DetectionOngoingEvent -> TriggerActivationEvent -> EndDetectEvent /\ /\ / ---------------------> CancelActivationEvent ----------------------/ |
| player_input | The per-player input manager. Get one for a player with 'GetPlayerInput', then use it to: Turn input mappings on or off for that player with 'AddInputMapping' / 'RemoveInputMapping'. Get the 'input_events' object for an 'input_action' with 'GetInputEvents', and subscribe to its events to react to that input. An input_action only generates events for a player while at least one input_mapping that references it is active on that player. |
| deproject_results | Holds the world-space ray produced by deprojecting a viewport coordinate. |

## Functions
| Name | Description |
| GetPlayerInput | Access input-related data and settings for a player. |
| input_events | Input_events is a container for user input events which can be subscribed to. Use the 'GetPlayerInput' and 'GetInputEvents' functions to retrieve an input_events object for a given player. Low-level notifications of current user input: BeginDetectEvent, DetectionOngoingEvent, and EndDetectEvent. High-level notifications of triggered events: TriggerActivationEvent and CancelActivationEvent. /—----------<-------\ BeginDetectEvent -> DetectionOngoingEvent -> TriggerActivationEvent -> EndDetectEvent /\ /\ / ---------------------> CancelActivationEvent ----------------------/ |

## Enumerations
| Name | Description |
| input_method | Represents the player's current preferred input method. |
