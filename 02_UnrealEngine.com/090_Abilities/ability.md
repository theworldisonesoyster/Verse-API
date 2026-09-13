---
name: ability
slug: unrealenginedotcom/abilities/ability
url: https://dev.epicgames.com/documentation/fortnite/verse-api/unrealenginedotcom/abilities/ability
kind: function
module: /Verse.org/abilities
grade: B
depth: brief
status: done
---

# ability function <B>

> Lives in the scene graph and is the high level description of an ability. Knows if an ability can run, cooldowns, distance and targeting requirements etc...
> 存在于场景图中，是技能的高层描述：知道技能能否运行、冷却、距离与目标要求等（构造函数）。

`using { /UnrealEngine.com/Abilities }`

```verse
ability<public>(context_type:ability_context, ability_effect_type:ability_effect):ability(context_type,ability_effect_type)
```

```verse
This function is a parametric type, meaning it returns a class or interface rather than a value or object instance.
```

## Parameters

ability 接受以下参数：
| Name | Type | Description |
| context_type | ability_context |  |
| ability_effect_type | ability_effect |  |

### Generated Class
ability 返回参数化类 ability(context_type,ability_effect_type)。

_（Attributes/Specifiers/Effects 公共说明见《Specifiers 与 Effects 对照》，此处不重复官网公共表格）_
