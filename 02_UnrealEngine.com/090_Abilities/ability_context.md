---
name: ability_context
slug: unrealenginedotcom/abilities/ability_context
url: https://dev.epicgames.com/documentation/fortnite/verse-api/unrealenginedotcom/abilities/ability_context
kind: class
module: /Verse.org/abilities
grade: B
depth: brief
status: done
---

# ability_context class <B>

> Data passed on activation of an ability. Holds who fired, who helped, and what got hit. Subclass to provide specific context for custom ability effects
> 技能激活时传入的数据：谁发起、谁协助、击中了什么。子类化它可为自定义技能效果提供上下文。

`using { /UnrealEngine.com/Abilities }`

## Members

只有数据成员，没有函数。

### Data
| Data Member Name | Type | Description |
| Instigator | ??agent | 发起该技能的代理。 |
| Participants | ?[]entity | 参与的代理列表。 |
| Targets | ?[]entity | 技能目标列表。 |
