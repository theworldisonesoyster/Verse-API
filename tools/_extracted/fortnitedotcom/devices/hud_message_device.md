Used to show custom HUD messages to one or more agents.
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
| ClearAllMessagesEvent | listenable(payload) | Called when all queued Messages from all players that are affected by this HUD Message Device have been cleared. |
| HideMessageEvent | listenable(payload) | Called when a Message has been Hidden on-screen. Returns an Agent if it was Hidden from a specified Agent's screen. |
| ShowMessageEvent | listenable(payload) | Called when a Message has been Shown on-screen. Returns an Agent if it was Shown on a specified Agent's screen. |

### Functions
| Function Name | Description |
| ClearAllMessages | Clears all queued Messages from all players that are affected by this HUD Message Device. |
| GetDisplayTime | Returns the time (in seconds) for which the HUD message will be displayed. 0.0 means the message is displayed persistently. |
| GetGlobalTransform | Gets the global transform of this object. |
| GetTransform | Returns the transform of the creative_object with units in cm. You must check creative_object.IsValid before calling this if there is a possibility the object has been disposed or destroyed by gameplay. Otherwise a runtime error will result. |
| Hide | Hides the HUD message. |
| Hide | Hides the currently set HUD Message on Agents screen. Use this when the device is setup to target specific agents. |
| MoveTo | Moves the creative_object to the specified Position and Rotation over the specified time, in seconds. If an animation is currently playing on the creative_object it will be stopped and put into the AnimationNotSet state. |
| MoveTo | Moves the creative_object to the specified Transform over the specified time, in seconds. If an animation is currently playing on the creative_object it will be stopped and put into the AnimationNotSet state. |
| MoveTo | Moves the creative_device to the specified Transform over the specified time, in seconds. If an animation is currently playing on the creative_device it will be stopped and put into the AnimationNotSet state. |
| SetDisplayTime | Sets the time (in seconds) the HUD message will be displayed. 0.0 will display the HUD message persistently. |
| SetGlobalTransform | Sets the global transform of this object. |
| SetText | Sets the Message to be displayed when the HUD message is activated. Text is clamped to 150 characters. |
| Show | Shows the currently set HUD Message on Agents screen. Will replace any previously active message. Use this when the device is setup to target specific agents. |
| Show | Shows the currently set Message HUD message on screen. Will replace any previously active message. |
| Show | Displays a Custom message to a specific Agent that you define.Setting DisplayTime to 0.0 will display the HUD message persistently.If not defined, or less than 0.0 the message will show for the time set on the device. |
| Show | Displays a Custom message that you define for all PlayersSetting DisplayTime to 0.0 will display the HUD message persistently.If not defined, or less than 0.0 the message will show for the time set on the device. |
| TeleportTo | Teleports the creative_object to the specified Position and Rotation. |
| TeleportTo | Teleports the creative_object to the specified location defined by Transform, also applies rotation and scale accordingly. |
| TeleportTo | Teleports the creative_device to the specified location defined by Transform, also applies rotation and scale accordingly. |
