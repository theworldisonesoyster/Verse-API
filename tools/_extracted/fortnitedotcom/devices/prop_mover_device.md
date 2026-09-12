Used to move around a building or prop, and customize responses to various collision event types.
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
| AgentHitEvent | listenable(payload) | Signaled when the prop hits an agent. Sends the agent hit by the prop. |
| AIHitEvent | listenable(payload) | Signaled when the prop hits a creature, animal, or NPC. |
| BeganEvent | listenable(payload) | Signaled when the prop movement begins. |
| DisabledEvent | listenable(payload) | Signaled when this device is disabled. |
| EnabledEvent | listenable(payload) | Signaled when this device is enabled. |
| EndedEvent | listenable(payload) | Signaled when the prop movement ends. |
| FinishedEvent | listenable(payload) | Signaled when the prop reaches its destination. |
| MovementModeChangedEvent | listenable(payload) | Signaled when the prop changes its direction. |
| PropHitEvent | listenable(payload) | Signaled when the prop hits another prop. |

### Functions
| Function Name | Description |
| Advance | Moves the prop forward based on this device's default configuration, ignoring the prop's previous movement. |
| Begin | Begins the prop moving. |
| Disable | Disables this device. |
| Enable | Enables this device. |
| End | Ends the prop moving. |
| GetGlobalTransform | Gets the global transform of this object. |
| GetTargetDistance | Returns the total distance (in meters) that the prop will move. |
| GetTargetSpeed | Returns the speed (in meters per second) at which the prop mover will move the prop to its destination. |
| GetTransform | Returns the transform of the creative_object with units in cm. You must check creative_object.IsValid before calling this if there is a possibility the object has been disposed or destroyed by gameplay. Otherwise a runtime error will result. |
| MoveTo | Moves the creative_object to the specified Position and Rotation over the specified time, in seconds. If an animation is currently playing on the creative_object it will be stopped and put into the AnimationNotSet state. |
| MoveTo | Moves the creative_object to the specified Transform over the specified time, in seconds. If an animation is currently playing on the creative_object it will be stopped and put into the AnimationNotSet state. |
| MoveTo | Moves the creative_device to the specified Transform over the specified time, in seconds. If an animation is currently playing on the creative_device it will be stopped and put into the AnimationNotSet state. |
| Reset | Moves the prop to its original position. |
| Reverse | Reverses the prop's moving direction. |
| SetGlobalTransform | Sets the global transform of this object. |
| SetTargetDistance | Sets the total distance (in meters) that the prop will move. |
| SetTargetSpeed | Sets the speed (in meters per second) at which the prop will move to its destination. |
| TeleportTo | Teleports the creative_object to the specified Position and Rotation. |
| TeleportTo | Teleports the creative_object to the specified location defined by Transform, also applies rotation and scale accordingly. |
| TeleportTo | Teleports the creative_device to the specified location defined by Transform, also applies rotation and scale accordingly. |
