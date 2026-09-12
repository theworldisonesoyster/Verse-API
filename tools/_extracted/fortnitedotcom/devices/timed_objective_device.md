Configures game modes where players can start or stop timers to advance gameplay objectives, such as Attack/Defend Bomb objectives.
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
| BeganEvent | listenable(payload) | Signaled when the objective begins. Sends the agent that started the timer. |
| CompletedEvent | listenable(payload) | Signaled when the objective is completed. Sends the agent that started the timer or completed the timer by calling Complete. |
| EndedEvent | listenable(payload) | Signaled when the objective ends. Sends the agent that stopped the timer. |
| PausedEvent | listenable(payload) | Signaled when the objective is paused. Sends the agent that paused the timer. |
| RestartedEvent | listenable(payload) | Signaled when the objective is restarted. Sends the agent that restarted the timer. |
| ResumedEvent | listenable(payload) | Signaled when the objective is resumed. Sends the agent that resumed the timer. |

### Functions
| Function Name | Description |
| Begin | Starts the objective with Agent acting as the user the interacted this device. |
| Complete | Completes the objective with Agent acting as the user the interacted this device. |
| Disable | Disables the objective for Agent. |
| Enable | Enables the objective for Agent. |
| End | Ends the objective with Agent acting as the user the interacted this device. |
| GetGlobalTransform | Gets the global transform of this object. |
| GetTransform | Returns the transform of the creative_object with units in cm. You must check creative_object.IsValid before calling this if there is a possibility the object has been disposed or destroyed by gameplay. Otherwise a runtime error will result. |
| Hide | Makes this device invisible. |
| MoveTo | Moves the creative_object to the specified Position and Rotation over the specified time, in seconds. If an animation is currently playing on the creative_object it will be stopped and put into the AnimationNotSet state. |
| MoveTo | Moves the creative_object to the specified Transform over the specified time, in seconds. If an animation is currently playing on the creative_object it will be stopped and put into the AnimationNotSet state. |
| MoveTo | Moves the creative_device to the specified Transform over the specified time, in seconds. If an animation is currently playing on the creative_device it will be stopped and put into the AnimationNotSet state. |
| Pause | Pauses the objective with Agent acting as the user the interacted this device. |
| Restart | Restarts the objective with Agent acting as the user the interacted this device. |
| Resume | Resumes the objective with Agent acting as the user the interacted this device. |
| SetGlobalTransform | Sets the global transform of this object. |
| Show | Makes this device visible. |
| TeleportTo | Teleports the creative_object to the specified Position and Rotation. |
| TeleportTo | Teleports the creative_object to the specified location defined by Transform, also applies rotation and scale accordingly. |
| TeleportTo | Teleports the creative_device to the specified location defined by Transform, also applies rotation and scale accordingly. |
