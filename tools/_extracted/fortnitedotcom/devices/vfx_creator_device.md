Used to create and customize your own visual effects. This is more flexible than the vfx_spawner_device, which gives you a selection of pre-made visual effects to choose from but limits how much you can customize or change those effects.
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
| Begin | Starts playing the effect. |
| Begin | Starts the effect at Agent's location. This option is only valid if Stick to Player is enabled. |
| BeginForAll | Starts the effect at every agent's location. This option is only valid if Stick to Player is enabled. |
| Disable | Disables this device. |
| Enable | Enables this device. |
| End | Ends playing the effect. |
| End | Ends the effect at Agent's location. This option is only valid if Stick to Player is enabled. |
| EndForAll | Ends the effect at every agent's locations. This option is only valid if Stick to Player is enabled. |
| GetGlobalTransform | Gets the global transform of this object. |
| GetTransform | Returns the transform of the creative_object with units in cm. You must check creative_object.IsValid before calling this if there is a possibility the object has been disposed or destroyed by gameplay. Otherwise a runtime error will result. |
| MoveTo | Moves the creative_object to the specified Position and Rotation over the specified time, in seconds. If an animation is currently playing on the creative_object it will be stopped and put into the AnimationNotSet state. |
| MoveTo | Moves the creative_object to the specified Transform over the specified time, in seconds. If an animation is currently playing on the creative_object it will be stopped and put into the AnimationNotSet state. |
| MoveTo | Moves the creative_device to the specified Transform over the specified time, in seconds. If an animation is currently playing on the creative_device it will be stopped and put into the AnimationNotSet state. |
| Remove | Removes the effect from Agent and continues playing at the device location. This option is only valid if Stick to Player is enabled. |
| RemoveFromAll | Removes the effect for every agent and continues playing at the device location. This option is only valid if Stick to Player is enabled. |
| SetGlobalTransform | Sets the global transform of this object. |
| SpawnAt | Spawns the effect at Agent's location. This option is only valid if Stick to Player is enabled. |
| TeleportTo | Teleports the creative_object to the specified Position and Rotation. |
| TeleportTo | Teleports the creative_object to the specified location defined by Transform, also applies rotation and scale accordingly. |
| TeleportTo | Teleports the creative_device to the specified location defined by Transform, also applies rotation and scale accordingly. |
| Toggle | Toggles between Begin and End. |
| Toggle | Toggles between Begin and End. |
| ToggleEnabled | Toggles between Enable and Disable. |
| ToggleForAll | Toggles between BeginForAll and EndForAll. |
| TogglePause | Pauses the effect if the effect is running. If the effect is paused, unpauses the effect. Pausing an effect causes the effect to freeze in place. |
| TogglePause | Pauses the effect at Agent's locations if it is playing, or resumes the effect if it is paused. When paused the effect freezes in place. |
| TogglePauseForAll | Pauses the effect at every agent's locations if it is playing, or resumes the effect if it is paused. When paused the effect freezes in place. |
