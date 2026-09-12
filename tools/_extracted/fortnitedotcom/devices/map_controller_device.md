Used to control the behavior of the map & minimap. Activation for a given agent can occur automatically via the device's Activate Automatically user option, by the agent entering and exiting the device's volume if using the Activate on Trigger user option, or via events from other devices or verse. When more than one map controller is activated for a given agent, the one with the highest Map Priority user option applies.
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
| Activate | Adds the map controller to the provided Agent's map controller stack. If multiple map controllers are active for an agent, the one with the highest Map Priority is used. |
| Activate | Adds the map controller to all agents in the experience. If multiple map controllers are active for an agent, the one with the highest Map Priority is used. |
| Deactivate | Removes the map controller from the provided Agent's map controller stack. The next highest priority active map controller will be used, or if none exists, the default behavior will be restored. |
| Deactivate | Removes the map controller from all agents in the experience. The next highest priority active map controller will be used, or if none exists, the default behavior will be restored. |
| Disable | Disables the device. Disabling the device will deactivate it for all agents in the experience, turn off the trigger functionality, and prevent it from responding to events. |
| Enable | Enables the device. Enabling the device will allow it to be activated, both by incoming events, and by trigger if using Activate on Trigger. |
| GetCaptureBoxSize | Returns the Capture Box Size (in meters). |
| GetGlobalTransform | Gets the global transform of this object. |
| GetTransform | Returns the transform of the creative_object with units in cm. You must check creative_object.IsValid before calling this if there is a possibility the object has been disposed or destroyed by gameplay. Otherwise a runtime error will result. |
| MoveTo | Moves the creative_object to the specified Position and Rotation over the specified time, in seconds. If an animation is currently playing on the creative_object it will be stopped and put into the AnimationNotSet state. |
| MoveTo | Moves the creative_object to the specified Transform over the specified time, in seconds. If an animation is currently playing on the creative_object it will be stopped and put into the AnimationNotSet state. |
| MoveTo | Moves the creative_device to the specified Transform over the specified time, in seconds. If an animation is currently playing on the creative_device it will be stopped and put into the AnimationNotSet state. |
| SetCaptureBoxSize | Sets the Capture Box Size (in meters). Capture Box Size refers to the length and width of the area used for both the map capture image as well as the activation trigger. Value is clamped between 25.0 and 2500.0 meters. |
| SetGlobalTransform | Sets the global transform of this object. |
| TeleportTo | Teleports the creative_object to the specified Position and Rotation. |
| TeleportTo | Teleports the creative_object to the specified location defined by Transform, also applies rotation and scale accordingly. |
| TeleportTo | Teleports the creative_device to the specified location defined by Transform, also applies rotation and scale accordingly. |
