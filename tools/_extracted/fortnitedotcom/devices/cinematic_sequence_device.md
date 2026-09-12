Used to trigger level sequences that allow coordination of cinematic animation, transformation, and audio tracks.
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
| StoppedEvent | listenable(payload) | Signaled when the sequence is stopped. |

### Functions
| Function Name | Description |
| GetGlobalTransform | Gets the global transform of this object. |
| GetPlaybackFrame | Returns the playback position (in frames) of the sequence. |
| GetPlaybackTime | Returns the playback position (in time/seconds) of the sequence. |
| GetPlayRate | Returns the playback rate of the sequence. |
| GetTransform | Returns the transform of the creative_object with units in cm. You must check creative_object.IsValid before calling this if there is a possibility the object has been disposed or destroyed by gameplay. Otherwise a runtime error will result. |
| GoToEndAndStop | Go to the end and stop the sequence. |
| GoToEndAndStop | Go to the end and stop the sequence. An instigating 'Agent' is required when the device is set to anything except Everyone. |
| MoveTo | Moves the creative_object to the specified Position and Rotation over the specified time, in seconds. If an animation is currently playing on the creative_object it will be stopped and put into the AnimationNotSet state. |
| MoveTo | Moves the creative_object to the specified Transform over the specified time, in seconds. If an animation is currently playing on the creative_object it will be stopped and put into the AnimationNotSet state. |
| MoveTo | Moves the creative_device to the specified Transform over the specified time, in seconds. If an animation is currently playing on the creative_device it will be stopped and put into the AnimationNotSet state. |
| Pause | Pauses the sequence. |
| Pause | Pauses the sequence. An instigating 'Agent' is required when the device is set to anything except Everyone. |
| Play | Plays the sequence. This will only work when the device is set to Everyone |
| Play | Plays the sequence. An instigating 'Agent' is required when the device is set to anything except Everyone. |
| PlayReverse | Plays the sequence in reverse. This will only work when the device is set to Everyone |
| PlayReverse | Plays the sequence in reverse. An instigating 'Agent' is required when the device is set to anything except Everyone. |
| SetGlobalTransform | Sets the global transform of this object. |
| SetPlaybackFrame | Set the playback position (in frames) of the sequence. |
| SetPlaybackTime | Set the playback position (in time/seconds) of the sequence. |
| SetPlayRate | Set the playback rate of the sequence. |
| Stop | Stops the sequence. |
| Stop | Stops the sequence. An instigating 'Agent' is required when the device is set to anything except Everyone. |
| TeleportTo | Teleports the creative_object to the specified Position and Rotation. |
| TeleportTo | Teleports the creative_object to the specified location defined by Transform, also applies rotation and scale accordingly. |
| TeleportTo | Teleports the creative_device to the specified location defined by Transform, also applies rotation and scale accordingly. |
| TogglePause | Toggles between Play and Stop. |
| TogglePause | Toggles between Play and Stop. An instigating 'Agent' is required when the device is set to anything except Everyone. |
