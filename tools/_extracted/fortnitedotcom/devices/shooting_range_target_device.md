A single customizable pop up target that can be hit by agents to trigger various events.
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
| BullseyeHitEvent | listenable(payload) | Signaled when the target is hit in the bullseye area. |
| HitEvent | listenable(payload) | Signaled when the target is hit by an agent. |
| HopDownEvent | listenable(payload) | Signaled when the target moves down slightly, making it harder to hit. |
| HopUpEvent | listenable(payload) | Signaled when the target moves up slightly, making it harder to hit. |
| KnockdownEvent | listenable(payload) | Signaled when the target takes enough damage to get knocked down. |
| PopDownEvent | listenable(payload) | Signaled when the target moves from standing upright to laying flat. |
| PopUpEvent | listenable(payload) | Signaled when the target moves from laying flat to standing upright. |

### Functions
| Function Name | Description |
| Disable | Disables this device. |
| Enable | Enables this device. |
| GetGlobalTransform | Gets the global transform of this object. |
| GetTransform | Returns the transform of the creative_object with units in cm. You must check creative_object.IsValid before calling this if there is a possibility the object has been disposed or destroyed by gameplay. Otherwise a runtime error will result. |
| HopDown | Moves an active (standing upright) target down slightly, in an effort to make it harder to hit. |
| HopUp | Moves an active (standing upright) target up slightly, in an effort to make it harder to hit. |
| MoveTo | Moves the creative_object to the specified Position and Rotation over the specified time, in seconds. If an animation is currently playing on the creative_object it will be stopped and put into the AnimationNotSet state. |
| MoveTo | Moves the creative_object to the specified Transform over the specified time, in seconds. If an animation is currently playing on the creative_object it will be stopped and put into the AnimationNotSet state. |
| MoveTo | Moves the creative_device to the specified Transform over the specified time, in seconds. If an animation is currently playing on the creative_device it will be stopped and put into the AnimationNotSet state. |
| PopDown | Causes a target to transition from standing upright (active) to lying flat (inactive). |
| PopUp | Causes a target to transition from lying flat (inactive) to standing upright (active). |
| Reset | Resets the target to its initial settings. |
| SetGlobalTransform | Sets the global transform of this object. |
| TeleportTo | Teleports the creative_object to the specified Position and Rotation. |
| TeleportTo | Teleports the creative_object to the specified location defined by Transform, also applies rotation and scale accordingly. |
| TeleportTo | Teleports the creative_device to the specified location defined by Transform, also applies rotation and scale accordingly. |
