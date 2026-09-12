A simplified storm device that provides a way to create a single-phase storm and control its basic behaviors. To control multiple phases of the storm see advanced_storm_controller_device.
|  |  |
| Verse using statement | using { /Fortnite.com/Devices } |

## Inheritance Hierarchy
This class is derived from the following hierarchy, starting with creative_object:
| Name | Description |
| creative_object | Base class for creative devices and props. |
| creative_device_base | Base class for creative_device. |
| storm_controller_device | Base class for various specialized storm devices. See also: basic_storm_controller_device advanced_storm_controller_device |

## Members
This class has both data members and functions.

### Data
| Data Member Name | Type | Description |
| PhaseEndedEvent | listenable(payload) | Signaled when storm resizing ends. Use this with the On Finish Behavior option for better controls. |

### Functions
| Function Name | Description |
| DestroyStorm | Destroys the storm. |
| GenerateStorm | Generates the storm. Generate Storm On Game Start must be set to No if you choose to use GenerateStorm. |
| GetGlobalTransform | Gets the global transform of this object. |
| GetTransform | Returns the transform of the creative_object with units in cm. You must check creative_object.IsValid before calling this if there is a possibility the object has been disposed or destroyed by gameplay. Otherwise a runtime error will result. |
| MoveTo | Moves the storm_controller_device to the specified Position and Rotation over the specified time, in seconds. Existing storms will not target the new location, but newly generated storms will. |
| MoveTo | Moves the storm_controller_device to the specified Transform over the specified time, in seconds. Existing storms will not target the new location, but newly generated storms will. |
| MoveTo | Moves the creative_object to the specified Position and Rotation over the specified time, in seconds. If an animation is currently playing on the creative_object it will be stopped and put into the AnimationNotSet state. |
| MoveTo | Moves the creative_object to the specified Transform over the specified time, in seconds. If an animation is currently playing on the creative_object it will be stopped and put into the AnimationNotSet state. |
| MoveTo | Moves the creative_device to the specified Transform over the specified time, in seconds. If an animation is currently playing on the creative_device it will be stopped and put into the AnimationNotSet state. |
| SetGlobalTransform | Sets the global transform of this object. |
| TeleportTo | Teleports the storm_controller_device to the specified Position and Rotation. Existing storms will not target the new location, but newly generated storms will. |
| TeleportTo | Teleports the storm_controller_device to the specified location defined by Transform, also applies rotation and scale accordingly. Existing storms will not target the new location, but newly generated storms will. |
| TeleportTo | Teleports the creative_object to the specified Position and Rotation. |
| TeleportTo | Teleports the creative_object to the specified location defined by Transform, also applies rotation and scale accordingly. |
| TeleportTo | Teleports the creative_device to the specified location defined by Transform, also applies rotation and scale accordingly. |
