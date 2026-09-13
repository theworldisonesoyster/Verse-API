---
name: remove_item_query_event
slug: unrealenginedotcom/itemization/remove_item_query_event
url: https://dev.epicgames.com/documentation/fortnite/verse-api/unrealenginedotcom/itemization/remove_item_query_event
kind: class
module: /UnrealEngine.com/itemization
grade: B
depth: brief
status: done
---

# remove_item_query_event class <B>

> Can be used to veto item removal. Sent upwards from the inventory (to its ancestors) and downwards from the item entity (to its children).
> 可用于否决物品移除：从物品栏（向祖先）向上、并从物品实体（向子级）向下发送。

`using { /UnrealEngine.com/Itemization }`

## Exposed Interfaces

此 暴露以下接口：
| Name | Description |
| scene_event | 可通过场景图发送的事件。 |


## Members

兼有数据成员和函数。

### Data
| Data Member Name | Type | Description |
| Item | item_component |  |
| Inventory | inventory_component |  |
| Errors | ?[]remove_item_error |  |

### Functions
| Function Name | Description |
| AddError |  |
