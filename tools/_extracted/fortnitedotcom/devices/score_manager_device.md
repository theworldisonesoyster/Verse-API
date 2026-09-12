Used to manipulate scores using in-experience triggers. If Activating Team is set to a specific team, then you should use the agent overloads of each function. The agent's team will be used to determine if that agent is allowed to affect the state of the device.
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
| MaxTriggersEvent | listenable(payload) | Signaled when the this device reaches its maximum number of triggers as defined by Times Can Trigger. Sends the agent who last triggered the device. |
| ScoreOutputEvent | listenable(payload) | Signaled when the this device awards points to an agent. Sends the agent who received the points. |

### Functions
| Function Name | Description |
| Activate | Grant points to Agent. |
| Activate | Grants points. |
| Decrement | Decrements the score quantity to be awarded by the next activation by 1. |
| Decrement | Decrements the score quantity to be awarded by the next activation by 1. |
| Disable | Disables this device. |
| Disable | Disables this device. |
| Enable | Enables this device. |
| Enable | Enables this device. |
| GetCurrentScore | Returns the current score for Agent. |
| GetGlobalTransform | Gets the global transform of this object. |
| GetScoreAward | Returns the score to be awarded by the next activation. |
| GetTransform | Returns the transform of the creative_object with units in cm. You must check creative_object.IsValid before calling this if there is a possibility the object has been disposed or destroyed by gameplay. Otherwise a runtime error will result. |
| Increment | Increments the score quantity to be awarded by the next activation by 1. |
| Increment | Increments the score quantity to be awarded by the next activation by 1. |
| MoveTo | Moves the creative_object to the specified Position and Rotation over the specified time, in seconds. If an animation is currently playing on the creative_object it will be stopped and put into the AnimationNotSet state. |
| MoveTo | Moves the creative_object to the specified Transform over the specified time, in seconds. If an animation is currently playing on the creative_object it will be stopped and put into the AnimationNotSet state. |
| MoveTo | Moves the creative_device to the specified Transform over the specified time, in seconds. If an animation is currently playing on the creative_device it will be stopped and put into the AnimationNotSet state. |
| Reset | Resets this device to its original state. |
| Reset | Resets this device to its original state. |
| SetGlobalTransform | Sets the global transform of this object. |
| SetScoreAward | Sets the score to be awarded by the next activation to Value. |
| SetToAgentScore | Sets the score to be awarded by the next activation to Agent's current score. |
| TeleportTo | Teleports the creative_object to the specified Position and Rotation. |
| TeleportTo | Teleports the creative_object to the specified location defined by Transform, also applies rotation and scale accordingly. |
| TeleportTo | Teleports the creative_device to the specified location defined by Transform, also applies rotation and scale accordingly. |
