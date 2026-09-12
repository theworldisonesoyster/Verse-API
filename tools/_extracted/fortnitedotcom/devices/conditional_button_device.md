Used to create a specialized button which can only be activated when agents are carrying specific items.
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
| ActivatedEvent | listenable(payload) | Signaled when this device is activated. Sends the agent that activated this device. |
| NotEnoughItemsEvent | listenable(payload) | Signaled when this device fails to activate because agent didn't have the required items. Sends the agent that attempted to activate the device. |

### Functions
| Function Name | Description |
| Activate | Activates this device. Agent is used as the instigator of the action. |
| Disable | Disables this device. |
| Enable | Enables this device. |
| GetGlobalTransform | Gets the global transform of this object. |
| GetInteractionTime | Returns the time (in seconds) that an interaction with this device will take to complete. |
| GetItemCount | Returns how many items an Agent has of the item stored at KeyItemIndex. |
| GetItemCountRequired | Returns the total quantity of a specific key item type that needs to be collected in order to activate the switch. |
| GetItemScore | Returns the score to be awarded for a key item. |
| GetRemainingItemCountRequired | Returns the remaining quantity of a specific key item type that needs to be collected in order to activate the switch. |
| GetTransform | Returns the transform of the creative_object with units in cm. You must check creative_object.IsValid before calling this if there is a possibility the object has been disposed or destroyed by gameplay. Otherwise a runtime error will result. |
| HasAllItems | Returns if the Agent has all of the items required to interact with this Device. |
| IsHoldingItem | Returns if the Agent is currently holding any of the items stored in the Device. |
| IsHoldingItem | Returns if the Agent is currently holding the item stored at KeyItemIndex. |
| MoveTo | Moves the creative_object to the specified Position and Rotation over the specified time, in seconds. If an animation is currently playing on the creative_object it will be stopped and put into the AnimationNotSet state. |
| MoveTo | Moves the creative_object to the specified Transform over the specified time, in seconds. If an animation is currently playing on the creative_object it will be stopped and put into the AnimationNotSet state. |
| MoveTo | Moves the creative_device to the specified Transform over the specified time, in seconds. If an animation is currently playing on the creative_device it will be stopped and put into the AnimationNotSet state. |
| Reset | Resets this device to its original settings. |
| SetGlobalTransform | Sets the global transform of this object. |
| SetInteractionText | Sets the text that appears when agents approach the device. Text is limited to 150 characters and will revert back to default if empty. |
| SetInteractionTime | Sets the time (in seconds) that an interaction with this device should take to complete. |
| SetItemCountRequired | Sets the quantity of a specific key item type that needs to be collected in order to activate the switch. KeyItemIndex ranges from 0 to number of key item types - 1. |
| SetItemScore | Sets the score to be awarded for a key item. KeyItemIndex ranges from 0 to number of key item types - 1. |
| TeleportTo | Teleports the creative_object to the specified Position and Rotation. |
| TeleportTo | Teleports the creative_object to the specified location defined by Transform, also applies rotation and scale accordingly. |
| TeleportTo | Teleports the creative_device to the specified location defined by Transform, also applies rotation and scale accordingly. |
| Toggle | Toggles the conditional button state. Agent is used as the instigator of the action. |
