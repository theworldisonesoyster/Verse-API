Used to create HUD text boxes that give players information, and allows responses to be customized to player choices.
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
| DismissedEvent | listenable(payload) | Signaled when this device is dismissed by an agent. Sends the agent who dismissed the popup. |
| RespondingButtonEvent | listenable(payload) | Signaled when Button on this device is pushed by an agent. Sends the agent that pushed the button. Sends the int index of the button that was clicked. |
| ShownEvent | listenable(payload) | Signaled when this device is shown to an agent. Sends the agent looking at the popup. |
| TimeOutEvent | listenable(payload) | Signaled when this device times out while an agent is looking at it. Sends the agent who was looking at the popup. |

### Functions
| Function Name | Description |
| Disable | Disables this device. |
| Enable | Enables this device. |
| GetButtonText | Returns the Button Text for this popup at a specified index. |
| GetDescriptionText | Returns the Description text for this popup. |
| GetGlobalTransform | Gets the global transform of this object. |
| GetTitleText | Returns the Title text for this popup. |
| GetTransform | Returns the transform of the creative_object with units in cm. You must check creative_object.IsValid before calling this if there is a possibility the object has been disposed or destroyed by gameplay. Otherwise a runtime error will result. |
| Hide | Hides the popup from Agent. |
| Hide | Hides the popup from all agents in the experience. |
| MoveTo | Moves the creative_object to the specified Position and Rotation over the specified time, in seconds. If an animation is currently playing on the creative_object it will be stopped and put into the AnimationNotSet state. |
| MoveTo | Moves the creative_object to the specified Transform over the specified time, in seconds. If an animation is currently playing on the creative_object it will be stopped and put into the AnimationNotSet state. |
| MoveTo | Moves the creative_device to the specified Transform over the specified time, in seconds. If an animation is currently playing on the creative_device it will be stopped and put into the AnimationNotSet state. |
| SetButtonCount | Sets the number of buttons this popup has. Button Count is not updated on active Popups. |
| SetButtonText | Sets the Button Text for a button at a specific index on this popup. Text should be no more than 24 characters. If Text is empty the button will show OK instead. Button 1 uses Index 0. |
| SetDescriptionText | Sets the Description text for this popup. Text should be no more than 350 characters. |
| SetGlobalTransform | Sets the global transform of this object. |
| SetTitleText | Sets the Title text for this popup. Text should be no more than 32 characters. |
| Show | Shows the popup to Agent. |
| Show | Shows the popup to all agents in the experience. |
| TeleportTo | Teleports the creative_object to the specified Position and Rotation. |
| TeleportTo | Teleports the creative_object to the specified location defined by Transform, also applies rotation and scale accordingly. |
| TeleportTo | Teleports the creative_device to the specified location defined by Transform, also applies rotation and scale accordingly. |
