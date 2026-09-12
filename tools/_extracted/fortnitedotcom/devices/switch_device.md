Used to allow agents to turn other linked devices on/off or other custom state changes.
|  |  |
| Verse using statement | using { /Fortnite.com/Devices } |

## Inheritance Hierarchy
This class is derived from the following hierarchy, starting with creative_object:
| Name | Description |
| creative_object | Base class for creative devices and props. |
| creative_device_base | Base class for creative_device. |

## Members
This class has both data members and functions.

### Data
| Data Member Name | Type | Description |
| ClearEvent | listenable(payload) | Signaled when the persistent data is cleared by the specified agent. Sends the agent that cleared persistent data on the device. |
| IfOffWhenCheckedEvent | listenable(payload) | Signaled if the switch is off when the state is checked. |
| IfOnWhenCheckedEvent | listenable(payload) | Signaled if the switch is on when the state is checked. |
| StateChangesEvent | listenable(payload) | Signaled when the switch state changes. |
| StateLoadEvent | listenable(payload) | Signaled when the switch state is loaded by the specified agent. Sends the agent that loaded the state on the device. |
| StateSaveEvent | listenable(payload) | Signaled when the switch state is saved. |
| TurnedOffEvent | listenable(payload) | Signaled when the switch is turned off by the specified agent. Sends the agent that turned off the device. |
| TurnedOnEvent | listenable(payload) | Signaled when the switch is turned on by the specified agent. Sends the agent that turned on the device. |

### Functions
| Function Name | Description |
| CheckState | Checks the device state with Agent acting as the instigator of the action. |
| ClearAllPersistenceData | Clears persistence data for all agents. |
| ClearPersistenceData | Clears persistence data for Agent. |
| Disable | Disables this device. |
| Enable | Enables this device. |
| GetCurrentResetTime | Returns the time, in seconds, before the switch will reset itself to default. Returns -1.0 if Store State Per Player is Yes or if there is no active reset timer. |
| GetCurrentResetTime | Returns the time, in seconds, before the switch will reset itself to default for Agent. Returns -1.0 if there is no active reset timer. |
| GetCurrentState | Succeeds if the current state of this switch is on, fails otherwise. Use this overload of GetCurrentState when this device has Store State Per Player set to Yes. |
| GetCurrentState | Succeeds if the current state of this switch is on, fails otherwise. Use this overload of GetCurrentState when this device has Store State Per Player set to No. |
| GetGlobalTransform | Gets the global transform of this object. |
| GetInteractionTime | Returns the Interaction Time required to activate this device (in seconds). |
| GetStateResetTime | Returns the value of State Reset Time, in seconds, for the device. Returns -1.0 if State Reset Time is not used. |
| GetStateResetTime | Returns the value of State Reset Time, in seconds, for the device, for a specific player. Returns -1.0 if State Reset Time is not used. |
| GetTransform | Returns the transform of the creative_object with units in cm. You must check creative_object.IsValid before calling this if there is a possibility the object has been disposed or destroyed by gameplay. Otherwise a runtime error will result. |
| IsStatePerAgent | Query whether this device has a single global on/off state, or has a personalized on/off state for each individual agent. |
| LoadState | Loads the device state with Agent acting as the instigator of the action. |
| LoadStateForAll | Loads the device state for all players. |
| MoveTo | Moves the creative_object to the specified Position and Rotation over the specified time, in seconds. If an animation is currently playing on the creative_object it will be stopped and put into the AnimationNotSet state. |
| MoveTo | Moves the creative_object to the specified Transform over the specified time, in seconds. If an animation is currently playing on the creative_object it will be stopped and put into the AnimationNotSet state. |
| MoveTo | Moves the creative_device to the specified Transform over the specified time, in seconds. If an animation is currently playing on the creative_device it will be stopped and put into the AnimationNotSet state. |
| SaveState | Saves the device state with Agent acting as the instigator of the action. |
| SaveStateForAll | Saves the device state for all players |
| SetGlobalTransform | Sets the global transform of this object. |
| SetInteractionTime | Sets the Interaction Time required to activate this device (in seconds). |
| SetState | Sets the state of the switch to a specific value for a specific Agent. Use when the device has Store State Per Player set to Yes. |
| SetState | Sets the state of the switch to a specific value. Use when the device has Store State Per Player set to No. |
| SetStateResetTime | Updates the State Reset Time for the device, in seconds, clamped to the Min and Max defined in the device. This will not apply to any state reset timers currently in effect. Set to 0.0 to disable the State Reset Time. Set to less than 0.0 to reset to default. |
| SetStateResetTime | Updates the State Reset Time for the device, in seconds,for a specific player (if Store State Per Player is Yes), clamped to the Min and Max defined in the device. This will not apply to any state reset timers currently in effect. Set to 0.0 to disable the State Reset Time. Set to less than 0.0 to reset to default. |
| SetTurnOffInteractionText | Sets the Turn Off Text to be displayed to a user when the switch is currently on, and offers an interaction to switch it off. Clamped to 150 characters. |
| SetTurnOnInteractionText | Sets the Turn On Text to be displayed to a user when the switch is currently off, and offers an interaction to switch it on. Clamped to 150 characters. |
| TeleportTo | Teleports the creative_object to the specified Position and Rotation. |
| TeleportTo | Teleports the creative_object to the specified location defined by Transform, also applies rotation and scale accordingly. |
| TeleportTo | Teleports the creative_device to the specified location defined by Transform, also applies rotation and scale accordingly. |
| ToggleState | Toggles between TurnOn and TurnOff with Agent acting as the instigator of the action. |
| TurnOff | Turns off the device with Agent acting as the instigator of the action. |
| TurnOn | Turns on this device with Agent acting as the instigator of the action. |
