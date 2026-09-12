Used to grant items to agents. Items can either be dropped at the agent's location or added directly to their inventory.
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
| DefaultItemCount | ?int | Gets or sets the default number of items that will be awarded for all items in the Item Granter that have not been overwritten. Count must be greater than 0. |
| GrantItemWithCountEvent | listenable(payload) | Signaled when an item is granted to an agent. Sends the agent that was granted the item, as well as the number of items granted. |
| ItemGrantedEvent | listenable(payload) | Signaled when an item is granted to an agent. Sends the agent that was granted the item. |

### Functions
| Function Name | Description |
| ClearSaveData | Clears saved data for Agent, preventing them from receiving items while offline. This only works when Grant While Offline is set to Yes. |
| CycleToNextItem | Cycles to the next item. If Grant on Cycle is set Agent will be granted the item. |
| CycleToPreviousItem | Cycles to the previous item. If Grant on Cycle is set Agent will be granted the item. |
| CycleToRandomItem | Cycles to a random item. If Grant on Cycle is set Agent will be granted the item. |
| Disable | Disables this device. |
| Enable | Enables this device. |
| GetGlobalTransform | Gets the global transform of this object. |
| GetItemGrantCountAtIndex | Returns the number of items this Item Granter will award for the item at the specified Index. This will return 0 if Index is invalid. If Cycle Behavior is Stop, Index is clamped to the number of items in the Item Granter. If Cycle Behavior is Wrap, Index is modulo'd to the number of items in the Item Granter. |
| GetItemIndex | Returns the current Item Index that this device will grant when activated. |
| GetTransform | Returns the transform of the creative_object with units in cm. You must check creative_object.IsValid before calling this if there is a possibility the object has been disposed or destroyed by gameplay. Otherwise a runtime error will result. |
| GrantItem | Grants an item to Agent. |
| GrantItemIndex | Grants an item at a specific ItemIndex to an Agent. Index should be between 0 and the available item count - 1. If Value is out of bounds, which item is granted is determined by Cycle Behavior. |
| GrantItemIndex | Grants an item at a specific ItemIndex to all players. Only functions when Receiving Players is set to All or Team Index. Index should be between 0 and the available item count - 1. If Value is out of bounds, which item is granted is determined by Cycle Behavior. |
| GrantItemToAll | Grants an item without requiring an agent reference. This only works when Receiving Players is set to All or Team Index. |
| MoveTo | Moves the creative_object to the specified Position and Rotation over the specified time, in seconds. If an animation is currently playing on the creative_object it will be stopped and put into the AnimationNotSet state. |
| MoveTo | Moves the creative_object to the specified Transform over the specified time, in seconds. If an animation is currently playing on the creative_object it will be stopped and put into the AnimationNotSet state. |
| MoveTo | Moves the creative_device to the specified Transform over the specified time, in seconds. If an animation is currently playing on the creative_device it will be stopped and put into the AnimationNotSet state. |
| RestockItems | Restocks this device back to its starting inventory count. |
| SetGlobalTransform | Sets the global transform of this object. |
| SetItemGrantCountAtIndex | Sets the number of items this Item Granter will award for the item at the specified ItemIndex. Count must be greater than 0. If Cycle Behavior is Stop, ItemIndex is clamped to the number of items in the Item Granter. If Cycle Behavior is Wrap, ItemIndex is modulo'd to the number of items in the Item Granter. |
| SetNextItem | Sets the next item to be granted. Index should be between 0 and the available item count - 1. Calling SetNextItem with an invalid index will do nothing. |
| TeleportTo | Teleports the creative_object to the specified Position and Rotation. |
| TeleportTo | Teleports the creative_object to the specified location defined by Transform, also applies rotation and scale accordingly. |
| TeleportTo | Teleports the creative_device to the specified location defined by Transform, also applies rotation and scale accordingly. |
