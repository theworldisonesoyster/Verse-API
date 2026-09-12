Inherit from this to create a custom creative device. Inherited classes will appear in the UEFN content browser the next time Verse compiles. Instances of your derived creative_device can then be placed in the island by dragging them from the content browser into the scene.
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
| OnBegin | Override to add custom logic when the game experience begins. |
| OnEnd | Override to add custom logic when the game experience ends. Any coroutines spawned inside OnEnd may never execute. |
| GetTransform | Returns the transform of the creative_device with units in cm. |
| TeleportTo | Teleports the creative_device to the specified Position and Rotation. |
| TeleportTo | Teleports the creative_device to the specified location defined by Transform, also applies rotation and scale accordingly. |
| MoveTo | Moves the creative_device to the specified Position and Rotation over the specified time, in seconds. If an animation is currently playing on the creative_device it will be stopped and put into the AnimationNotSet state. |
| MoveTo | Moves the creative_device to the specified Transform over the specified time, in seconds. If an animation is currently playing on the creative_device it will be stopped and put into the AnimationNotSet state. |
| GetGlobalTransform | Gets the global transform of this device. |
| SetGlobalTransform | Sets the global transform of this device. |
| TeleportTo | Teleports the creative_device to the specified location defined by Transform, also applies rotation and scale accordingly. |
| MoveTo | Moves the creative_device to the specified Transform over the specified time, in seconds. If an animation is currently playing on the creative_device it will be stopped and put into the AnimationNotSet state. |
| Show | Shows this device in the world. |
| Hide | Hides this device in the world. |
