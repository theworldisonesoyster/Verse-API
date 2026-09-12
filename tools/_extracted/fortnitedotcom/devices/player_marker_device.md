Used to mark an agent's position on the minimap and configure the information shown for marked agents.
Example configuration options:
- Health and shield bars for marked players.
- Distance to a marked player.
Example marker appearance options:
- Customized text label displayed on marked players.
- Alternative minimap icon and icon color.
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
| FirstItemValueChangedEvent | listenable(payload) | Signaled when the first item type monitored on marked agents has changed. Sends the marked agent. |
| FirstItemValueReachedEvent | listenable(payload) | Signaled when a marked agent meets the quantity condition for the first monitored item type (e.g. Fewer Than, Equal To, More Than X). Sends the marked agent. |
| SecondItemValueChangedEvent | listenable(payload) | Signaled when the second item type monitored on marked agents has changed. Sends the marked agent. |
| SecondItemValueReachedEvent | listenable(payload) | Signaled when a marked agent meets the quantity condition for the second monitored item type (e.g. Fewer Than, Equal To, More Than X). Sends the marked agent. |

### Functions
| Function Name | Description |
| Attach | Attaches a marker to Agent. |
| Detach | Detaches a marker from Agent. |
| DetachFromAll | Detaches markers from all marked agents. |
| Disable | Disables this device. |
| Enable | Enables this device. |
| GetGlobalTransform | Gets the global transform of this object. |
| GetTransform | Returns the transform of the creative_object with units in cm. You must check creative_object.IsValid before calling this if there is a possibility the object has been disposed or destroyed by gameplay. Otherwise a runtime error will result. |
| MoveTo | Moves the creative_object to the specified Position and Rotation over the specified time, in seconds. If an animation is currently playing on the creative_object it will be stopped and put into the AnimationNotSet state. |
| MoveTo | Moves the creative_object to the specified Transform over the specified time, in seconds. If an animation is currently playing on the creative_object it will be stopped and put into the AnimationNotSet state. |
| MoveTo | Moves the creative_device to the specified Transform over the specified time, in seconds. If an animation is currently playing on the creative_device it will be stopped and put into the AnimationNotSet state. |
| SetGlobalTransform | Sets the global transform of this object. |
| TeleportTo | Teleports the creative_object to the specified Position and Rotation. |
| TeleportTo | Teleports the creative_object to the specified location defined by Transform, also applies rotation and scale accordingly. |
| TeleportTo | Teleports the creative_device to the specified location defined by Transform, also applies rotation and scale accordingly. |
