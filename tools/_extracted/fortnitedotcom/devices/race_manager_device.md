Used with the race_checkpoint_device to create more advanced racing modes.
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
| FirstLapCompletedEvent | listenable(payload) | Signaled when an agent completes their first lap. Sends the agent that finished the lap. |
| LapCompletedEvent | listenable(payload) | Signaled when an agent completes a lap. Sends the agent that finished the lap. |
| RaceBeganEvent | listenable(payload) | Signaled when the race begins. Sends the agent that started the race. |
| RaceCompletedEvent | listenable(payload) | Signaled when an agent finishes the race. Sends the agent that finished the race. |

### Functions
| Function Name | Description |
| Begin | Begins the race. |
| Disable | Disables this device. |
| Enable | Enables this device. |
| End | Ends the race. |
| GetGlobalTransform | Gets the global transform of this object. |
| GetTransform | Returns the transform of the creative_object with units in cm. You must check creative_object.IsValid before calling this if there is a possibility the object has been disposed or destroyed by gameplay. Otherwise a runtime error will result. |
| MoveTo | Moves the creative_object to the specified Position and Rotation over the specified time, in seconds. If an animation is currently playing on the creative_object it will be stopped and put into the AnimationNotSet state. |
| MoveTo | Moves the creative_object to the specified Transform over the specified time, in seconds. If an animation is currently playing on the creative_object it will be stopped and put into the AnimationNotSet state. |
| MoveTo | Moves the creative_device to the specified Transform over the specified time, in seconds. If an animation is currently playing on the creative_device it will be stopped and put into the AnimationNotSet state. |
| SetGlobalTransform | Sets the global transform of this object. |
| TeleportTo | Teleports the creative_object to the specified Position and Rotation. |
| TeleportTo | Teleports the creative_object to the specified location defined by Transform, also applies rotation and scale accordingly. |
| TeleportTo | Teleports the creative_device to the specified location defined by Transform, also applies rotation and scale accordingly. |
