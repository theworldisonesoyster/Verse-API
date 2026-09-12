When unequipping an item, 'unequip_item_query_event' can be used to veto the unequip. It is sent upwards from the inventory (to its ancestors) and downwards from the item entity (to its children).
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
| Errors | ?[]unequip_item_error |  |

### Functions
| Function Name | Description |
| AddError |  |
