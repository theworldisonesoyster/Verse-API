- UnrealEngine.com
- Itemization

## Classes and Structs
| Name | Description |
| add_item_result |  |
| remove_item_result |  |
| equip_item_result |  |
| unequip_item_result |  |
| find_inventory_event | When adding an item, 'find_inventory_event' is used as a first pass to find the best inventory for an item. It is sent downwards. 'add_item_query_event' can be used to veto inventory choices. It is sent upwards. |
| add_item_error |  |
| add_item_query_event | When adding an item, 'find_inventory_event' is used as a first pass to find the best inventory for an item. It is sent downwards. 'add_item_query_event' can be used to veto inventory choices, sent upwards from the inventory (to its ancestors) and downwards from the item entity (to its children). |
| remove_item_error |  |
| remove_item_query_event | Can be used to veto item removal. Sent upwards from the inventory (to its ancestors) and downwards from the item entity (to its children). |
| inventory_component | Inventory components hold items. An entity with an inventory component can be considered to have an inventory. The inventory component controls which items can enter or exit. They also determine whether an item can be equipped. |
| item_category | item_category is used to classify items. |
| change_equipped_result |  |
| change_inventory_result |  |
| equip_item_error |  |
| equip_item_query_event | When equipping an item, 'equip_item_query_event' can be used to veto the equip. It is sent upwards from the inventory (to its ancestors) and downwards from the item entity (to its children). |
| unequip_item_error |  |
| unequip_item_query_event | When unequipping an item, 'unequip_item_query_event' can be used to veto the unequip. It is sent upwards from the inventory (to its ancestors) and downwards from the item entity (to its children). |
| item_component | Anything using this component should be considered an item. Required to interact with inventories. |
