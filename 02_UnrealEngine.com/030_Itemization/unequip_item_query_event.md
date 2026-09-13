---
name: unequip_item_query_event
slug: unrealenginedotcom/itemization/unequip_item_query_event
url: https://dev.epicgames.com/documentation/fortnite/verse-api/unrealenginedotcom/itemization/unequip_item_query_event
kind: class
module: /UnrealEngine.com/itemization
grade: B
depth: brief
status: done
---

# unequip_item_query_event class <B>

> When unequipping an item, 'unequip_item_query_event' can be used to veto the unequip. It is sent upwards from the inventory (to its ancestors) and downwards from the item entity (to its children).
> 卸下物品时可用于否决卸下：从物品栏（向祖先）向上、并从物品实体（向子级）向下发送。

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
| Errors | ?[]unequip_item_error |  |

### Functions
| Function Name | Description |
| AddError |  |
