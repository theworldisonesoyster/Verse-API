Base class for creative devices and props.
|  |  |
| Verse using statement | using { /Fortnite.com/Devices } |

## Exposed Interfaces
This class exposes the following interfaces:
| Name | Description |
| creative_object_interface |  |

## Members
This class has functions, but no data members.

### Functions
| Function Name | Description |
| GetTransform | Returns the transform of the creative_object with units in cm. You must check creative_object.IsValid before calling this if there is a possibility the object has been disposed or destroyed by gameplay. Otherwise a runtime error will result. |
| TeleportTo | Teleports the creative_object to the specified Position and Rotation. |
| TeleportTo | Teleports the creative_object to the specified location defined by Transform, also applies rotation and scale accordingly. |
| MoveTo | Moves the creative_object to the specified Position and Rotation over the specified time, in seconds. If an animation is currently playing on the creative_object it will be stopped and put into the AnimationNotSet state. |
| MoveTo | Moves the creative_object to the specified Transform over the specified time, in seconds. If an animation is currently playing on the creative_object it will be stopped and put into the AnimationNotSet state. |
| GetGlobalTransform | Gets the global transform of this object. |
| SetGlobalTransform | Sets the global transform of this object. |
| TeleportTo | Teleports the creative_device to the specified location defined by Transform, also applies rotation and scale accordingly. |
| MoveTo | Moves the creative_device to the specified Transform over the specified time, in seconds. If an animation is currently playing on the creative_device it will be stopped and put into the AnimationNotSet state. |
