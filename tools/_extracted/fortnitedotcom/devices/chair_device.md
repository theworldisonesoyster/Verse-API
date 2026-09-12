Creates a chair where Agents can sit.
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
| ExitedEvent | listenable(payload) | Signaled when an agent stops sitting on the Chair. Sends the standing Agent. |
| SeatedEvent | listenable(payload) | Signaled when an agent sits on the Chair. Sends the sitting agent. |

### Functions
| Function Name | Description |
| Disable | Disables the Chair. A disabled Chair cannot be interacted with and any agent currently occupying the Chair will be ejected. |
| DisableExit | Prevents any seated agent from leaving the Chair manually. While Exit is disabled, call Eject to force them out. |
| Eject | Ejects any agent currently in the chair. |
| Eject | Makes Agent exit this chair if they are currently in the chair. |
| Enable | Enables the Chair. An enabled Chair can be interacted with and occupied by any agent that meets the requirements. |
| EnableExit | Allows any seated agent to leave the chair manually. |
| GetGlobalTransform | Gets the global transform of this object. |
| GetSeatedAgent | Returns the agent currently occupying the chair. |
| GetTransform | Returns the transform of the creative_object with units in cm. You must check creative_object.IsValid before calling this if there is a possibility the object has been disposed or destroyed by gameplay. Otherwise a runtime error will result. |
| IsOccupied | Succeeds if the chair is currently occupied. |
| IsSeated | Succeeds if Agent is currently in the chair . |
| MoveTo | Moves the creative_object to the specified Position and Rotation over the specified time, in seconds. If an animation is currently playing on the creative_object it will be stopped and put into the AnimationNotSet state. |
| MoveTo | Moves the creative_object to the specified Transform over the specified time, in seconds. If an animation is currently playing on the creative_object it will be stopped and put into the AnimationNotSet state. |
| MoveTo | Moves the creative_device to the specified Transform over the specified time, in seconds. If an animation is currently playing on the creative_device it will be stopped and put into the AnimationNotSet state. |
| Seat | Makes Agent sit on this chair if they meet the requirements. |
| SetGlobalTransform | Sets the global transform of this object. |
| TeleportTo | Teleports the creative_object to the specified Position and Rotation. |
| TeleportTo | Teleports the creative_object to the specified location defined by Transform, also applies rotation and scale accordingly. |
| TeleportTo | Teleports the creative_device to the specified location defined by Transform, also applies rotation and scale accordingly. |
