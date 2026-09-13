---
name: ability(context_type,ability_effect_type)
slug: unrealenginedotcom/abilities/ability/ability(context_type,ability_effect_type)
url: https://dev.epicgames.com/documentation/fortnite/verse-api/unrealenginedotcom/abilities/ability/ability(context_type,ability_effect_type)
kind: class
module: /UnrealEngine.com/abilities/ability
grade: B
depth: brief
status: done
---

# ability(context_type,ability_effect_type) class <B>

> Lives in the scene graph and is the high level description of an ability. Knows if an ability can run, cooldowns, distance and targeting requirements etc...
> 存在于场景图中，是技能的高层描述：知道技能能否运行、冷却、距离与目标要求等。

`using { /UnrealEngine.com/Abilities }`

## Exposed Interfaces

此 暴露以下接口：
| Name | Description |
| has_icon | 提供图标的接口。 |


## Members

兼有数据成员和函数。

### Data
| Data Member Name | Type | Description |
| BeginUseEvent | listenable(payload) |  |
| EndUseEvent | listenable(payload) |  |
| ActiveEffects | ?[] |  |
| Icon | ?texture |  |

### Functions
| Function Name | Description |
| Use |  |
| CanUse |  |
| MakeContext |  |
| MakeAbility |  |
