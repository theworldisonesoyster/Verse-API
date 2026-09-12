Used to apply Post Process Effects to players through the creative device rather than a Post Process Volume.
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
| BlendingInCompleteEvent | listenable(payload) | Signaled when a blend in event has finished. Sends the agent that used this device. |
| BlendingOutCompleteEvent | listenable(payload) | Signaled when a blend out event has finished. Sends the agent that used this device. |

### Functions
| Function Name | Description |
| BlendIn | Starts blending in the post process effect to the set strength only for the instigating Agent. |
| BlendInForAll | Starts blending in the post process effect to the set strength for all players. |
| BlendOut | Starts blending out the post process effect to 0 strength only for the instigating Agent. |
| BlendOutForAll | Starts blending out the post process effect to 0 strength for all players. |
| Disable | Disables this device only for the instigating Agent. |
| Disable | Disables this device for all players. |
| Enable | Enables this device only for the instigating Agent. |
| Enable | Enables this device for all players. |
| GetGlobalTransform | Gets the global transform of this object. |
| GetTransform | Returns the transform of the creative_object with units in cm. You must check creative_object.IsValid before calling this if there is a possibility the object has been disposed or destroyed by gameplay. Otherwise a runtime error will result. |
| MoveTo | Moves the creative_object to the specified Position and Rotation over the specified time, in seconds. If an animation is currently playing on the creative_object it will be stopped and put into the AnimationNotSet state. |
| MoveTo | Moves the creative_object to the specified Transform over the specified time, in seconds. If an animation is currently playing on the creative_object it will be stopped and put into the AnimationNotSet state. |
| MoveTo | Moves the creative_device to the specified Transform over the specified time, in seconds. If an animation is currently playing on the creative_device it will be stopped and put into the AnimationNotSet state. |
| Reset | Resets to the starting strength, ending any ongoing blending only for the instigating Agent. |
| ResetForAll | Resets to the starting strength, ending any ongoing blending for all players. |
| SetGlobalTransform | Sets the global transform of this object. |
| TeleportTo | Teleports the creative_object to the specified Position and Rotation. |
| TeleportTo | Teleports the creative_object to the specified location defined by Transform, also applies rotation and scale accordingly. |
| TeleportTo | Teleports the creative_device to the specified location defined by Transform, also applies rotation and scale accordingly. |
