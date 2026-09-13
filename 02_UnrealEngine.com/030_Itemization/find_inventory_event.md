---
name: find_inventory_event
slug: unrealenginedotcom/itemization/find_inventory_event
url: https://dev.epicgames.com/documentation/fortnite/verse-api/unrealenginedotcom/itemization/find_inventory_event
kind: class
module: /UnrealEngine.com/itemization
grade: B
depth: brief
status: done
---

# find_inventory_event class <B>

> When adding an item, 'find_inventory_event' is used as a first pass to find the best inventory for an item. It is sent downwards. 'add_item_query_event' can be used to veto inventory choices. It is sent upwards.
> 添加物品时，find_inventory_event 作为第一道流程向下发送，用于为物品寻找最合适的物品栏；add_item_query_event 可否决物品栏选择（向上发送）。

`using { /UnrealEngine.com/Itemization }`

## Exposed Interfaces

此 暴露以下接口：
| Name | Description |
| scene_event | 可通过场景图发送的事件。 |


## Members

只有数据成员，没有函数。

### Data
| Data Member Name | Type | Description |
| ItemComponent | item_component | 候选的物品栏组件。 |
| ChosenInventory | ??inventory_component | 被选中的物品栏。 |
| ChosenInventoryPriority | ?float | 被选中物品栏的优先级。 |
