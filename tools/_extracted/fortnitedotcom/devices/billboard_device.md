Used to display custom text messages on a billboard.
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
| GetGlobalTransform | Gets the global transform of this object. |
| GetShowBorder | Returns true if the device border is enabled. |
| GetTextSize | Returns the Text Size of the device Text. |
| GetTransform | Returns the transform of the creative_object with units in cm. You must check creative_object.IsValid before calling this if there is a possibility the object has been disposed or destroyed by gameplay. Otherwise a runtime error will result. |
| HideText | Hides the billboard text. |
| MoveTo | Moves the creative_object to the specified Position and Rotation over the specified time, in seconds. If an animation is currently playing on the creative_object it will be stopped and put into the AnimationNotSet state. |
| MoveTo | Moves the creative_object to the specified Transform over the specified time, in seconds. If an animation is currently playing on the creative_object it will be stopped and put into the AnimationNotSet state. |
| MoveTo | Moves the creative_device to the specified Transform over the specified time, in seconds. If an animation is currently playing on the creative_device it will be stopped and put into the AnimationNotSet state. |
| SetGlobalTransform | Sets the global transform of this object. |
| SetShowBorder | Sets the visibility of the device border mesh. This also determines whether the device collision is enabled. |
| SetText | Sets the device Text. |
| SetTextSize | Sets the Text Size of the device Text. Clamped to range [8, 24]. |
| ShowText | Shows the billboard text. |
| TeleportTo | Teleports the creative_object to the specified Position and Rotation. |
| TeleportTo | Teleports the creative_object to the specified location defined by Transform, also applies rotation and scale accordingly. |
| TeleportTo | Teleports the creative_device to the specified location defined by Transform, also applies rotation and scale accordingly. |
| UpdateDisplay | Updates the device display to show the current Text. |
