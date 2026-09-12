When adding an item, 'find_inventory_event' is used as a first pass to find the best inventory for an item. It is sent downwards. 'add_item_query_event' can be used to veto inventory choices, sent upwards from the inventory (to its ancestors) and downwards from the item entity (to its children).
|  |  |
| Verse using statement | using { /UnrealEngine.com/Itemization } |

## Exposed Interfaces
This class exposes the following interfaces:
| Name | Description |
| scene_event | An event which can be sent through the scene graph. |

## Members
This class has both data members and functions.

### Data
| Data Member Name | Type | Description |
| Item | item_component |  |
| Inventory | inventory_component |  |
| Errors | ?[]add_item_error |  |

### Functions
| Function Name | Description |
| AddError |  |
