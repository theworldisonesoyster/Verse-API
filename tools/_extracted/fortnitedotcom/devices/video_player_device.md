Used to display curated videos onto in-game screens or player HUDs.
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
| StreamStartedEvent | listenable(payload) | Signaled when this device becomes the controlling streaming device for the agent. |

### Functions
| Function Name | Description |
| Disable | Disables this device. |
| DisableCollision | Disables collision checks on this device. |
| Enable | Enables this device. |
| EnableCollision | Enables collision checks on this device. |
| EndForAll | Turns off all streaming devices of this type on the island. |
| EnterFullScreen | Transitions to fullscreen for Agent. |
| ExitFullScreen | Transitions to fullscreen for Agent. |
| GetGlobalTransform | Gets the global transform of this object. |
| GetTransform | Returns the transform of the creative_object with units in cm. You must check creative_object.IsValid before calling this if there is a possibility the object has been disposed or destroyed by gameplay. Otherwise a runtime error will result. |
| HidePIP | Hides the picture-in-picture video from Agent. |
| MakePIPDefaultSize | Transitions the picture-in-picture video to the default size for Agent. |
| MakePIPFullScreen | Transitions the picture-in-picture video to full screen for Agent. |
| MoveTo | Moves the creative_object to the specified Position and Rotation over the specified time, in seconds. If an animation is currently playing on the creative_object it will be stopped and put into the AnimationNotSet state. |
| MoveTo | Moves the creative_object to the specified Transform over the specified time, in seconds. If an animation is currently playing on the creative_object it will be stopped and put into the AnimationNotSet state. |
| MoveTo | Moves the creative_device to the specified Transform over the specified time, in seconds. If an animation is currently playing on the creative_device it will be stopped and put into the AnimationNotSet state. |
| ReleaseControl | If any streaming device has forced control of the stream, this will release it and play the highest priority stream in line. |
| Restart | Restart the stream from the beginning. |
| Seek | Seeks to the Triggered Seek Time. Caution: The stream will pause while the video buffers when seeking. |
| SetGlobalTransform | Sets the global transform of this object. |
| TakeControl | Stops the currently playing stream and starts the custom stream with the audio only playing from this device. Stream Priority will not work until control is released. |
| TeleportTo | Teleports the creative_object to the specified Position and Rotation. |
| TeleportTo | Teleports the creative_object to the specified location defined by Transform, also applies rotation and scale accordingly. |
| TeleportTo | Teleports the creative_device to the specified location defined by Transform, also applies rotation and scale accordingly. |
