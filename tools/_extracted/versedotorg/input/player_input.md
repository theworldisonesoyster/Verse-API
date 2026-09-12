The per-player input manager. Get one for a player with 'GetPlayerInput', then use it to: Turn input mappings on or off for that player with 'AddInputMapping' / 'RemoveInputMapping'. Get the 'input_events' object for an 'input_action' with 'GetInputEvents', and subscribe to its events to react to that input. An input_action only generates events for a player while at least one input_mapping that references it is active on that player.
|  |  |
| Verse using statement | using { /Verse.org/Input } |

## Members
This class has both data members and functions.

### Data
| Data Member Name | Type | Description |
| PreferredInputMethod | ?input_method | The player's current preferred input method, updated when the player switches between keyboard/mouse, gamepad, or touch. |
| AvailableInputDevices | ?available_input_devices | The set of input device capabilities currently available to the player, updated at runtime as devices connect or disconnect. |

### Functions
| Function Name | Description |
| AddInputMapping | Adds the given input_mapping to the player, enabling the input_actions within it to be processed and execute events. |
| RemoveInputMapping | Removes the given input_mapping from the player, which will disable the input_actions within it from being processed and prevent them from executing events. |
| GetInputEvents | Returns the input_events object for the given input_action, allowing you to bind to events for this action. |
