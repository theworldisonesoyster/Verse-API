---
name: add_item_query_event
slug: unrealenginedotcom/itemization/add_item_query_event
url: https://dev.epicgames.com/documentation/fortnite/verse-api/unrealenginedotcom/itemization/add_item_query_event
kind: class
module: /UnrealEngine.com/itemization
grade: B
depth: brief
status: done
---

# add_item_query_event class <B>

> When adding an item, 'find_inventory_event' is used as a first pass to find the best inventory for an item. It is sent downwards. 'add_item_query_event' can be used to veto inventory choices, sent upwards from the inventory (to its ancestors) and downwards from the item entity (to its children).
> 添加物品时，find_inventory_event 先向下发送以寻找最佳物品栏；add_item_query_event 可否决物品栏选择——从物品栏（向祖先）向上、并从物品实体（向子级）向下发送。

`using { /UnrealEngine.com/Itemization }`

## Exposed Interfaces

此 暴露以下接口：
| Name | Description |
| scene_event | 可通过场景图发送的事件。 |


## Members

兼有数据成员和函数。

### Data
| Data Member Name | Type | Description |
| Item | item_component | 相关物品实体。 |
| Inventory | inventory_component | 相关物品栏组件。 |
| Errors | ?[]add_item_error | 查询后收集到的错误列表。 |

### Functions
| Function Name | Description |
| AddError |  |
