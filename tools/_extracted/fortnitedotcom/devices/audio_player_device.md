Used to configure and play audio from the device location or from registered agents.
|  |  |
| Verse using statement | using { /Fortnite.com/Devices } |

## Inheritance Hierarchy
This class is derived from the following hierarchy, starting with creative_object:
| Name | Description |
| creative_object | Base class for creative devices and props. |
| creative_device_base | Base class for creative_device. |

## Members
This class has functions, but no data members.

### Functions
| Function Name | Description |
| Disable | Disables this device. No longer allows this device to be triggered from other linked devices (i.e. triggers) and will stop any currently playing audio. |
| Enable | Enables this device. Allows this device to be triggered from other linked devices (i.e. triggers) and allow calls to Play to succeed. |
| GetGlobalTransform | Gets the global transform of this object. |
| GetTransform | Returns the transform of the creative_object with units in cm. You must check creative_object.IsValid before calling this if there is a possibility the object has been disposed or destroyed by gameplay. Otherwise a runtime error will result. |
| Hide | Hides this device from the world. |
| MoveTo | Moves the creative_object to the specified Position and Rotation over the specified time, in seconds. If an animation is currently playing on the creative_object it will be stopped and put into the AnimationNotSet state. |
| MoveTo | Moves the creative_object to the specified Transform over the specified time, in seconds. If an animation is currently playing on the creative_object it will be stopped and put into the AnimationNotSet state. |
| MoveTo | Moves the creative_device to the specified Transform over the specified time, in seconds. If an animation is currently playing on the creative_device it will be stopped and put into the AnimationNotSet state. |
| Play | Starts playing audio from this device for Agent. This can only be used when the device is set to be Heard by Instigator. |
| Play | Starts playing audio from this device. |
| Register | Adds Agent as a target to play audio from when activated. |
| SetGlobalTransform | Sets the global transform of this object. |
| Show | Shows this device in the world. |
| Stop | Stops any audio playing from this device for Agent. This can only be used when the device is set to be Heard by Instigator. |
| Stop | Stops any audio playing from this device. |
| TeleportTo | Teleports the creative_object to the specified Position and Rotation. |
| TeleportTo | Teleports the creative_object to the specified location defined by Transform, also applies rotation and scale accordingly. |
| TeleportTo | Teleports the creative_device to the specified location defined by Transform, also applies rotation and scale accordingly. |
| Unregister | Removes Agent as a target to play audio from when activated. |
| UnregisterAll | Removes all previously registered agents as valid targets to play audio from when activated. |
