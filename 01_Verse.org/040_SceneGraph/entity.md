---
name: entity
slug: versedotorg/scenegraph/entity
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/entity
kind: class
module: /Verse.org/SceneGraph
grade: S
depth: full
status: done
---

# entity 🟦【S级·核心】

> Entities are the base object in the SceneGraph. Objects in experiences are constructed of one or more entities.
> 实体是 SceneGraph 的基础对象——体验中的一切由一个或多个实体构成。

## 这是什么

SceneGraph 是 Epic 新一代场景对象模型（也是"迁移进 Verse.org"的那套体系），`entity` 是它的"空壳节点"：

- **有层级**：父实体管理子实体的生命周期（父被移除，子全移除）；`GetParent`/`AddEntities`/`RemoveFromParent` 维护这棵树。
- **能力靠组件**：行为/数据通过挂 [component](component.md)（如 [transform_component](transform_component.md)、mesh_component）添加，`AddComponents`/`GetComponent` 增查。
- **动态**：运行时随时增删子实体与组件。
- 继承 entity 的自定义类就是**预制体（prefab）**——官方建议通过编辑器生成，不要手写派生代码。

## 签名

```verse
entity<public><native> := class<native>:
    # 核心函数（官方摘录）
    GetParent<public>()<transacts><decides>:entity        # 取父实体（无父则失败）
    AddEntities<public>(Entities:[]entity):void           # 添加子实体
    RemoveFromParent<public>():void                       # 从父实体移除
    GetEntities<public>()<transacts>:[]entity             # 直接子实体
    GetComponent<public>()<transacts><decides>:component_type  # 按类型取组件
    AddComponents<public>(Components:[]component):void    # 添加组件
```

## 最小示例

```verse
using { /Verse.org/SceneGraph }

# 运行时搭一个"灯杆"：实体 + 变换 + 光源组件
BuildLamp(Parent:entity):void =
    Pole := entity{}
    Pole.AddComponents(array{transform_component{}, spot_light_component{}})
    Parent.AddEntities(array{Pole})
```

## 常用成员

| 成员 | 说明 | 级别 |
|---|---|---|
| `GetParent[]` | 取父（可失败） | 🟦 S |
| `AddEntities` / `RemoveFromParent` | 维护层级 | 🟦 S |
| `AddComponents` / `GetComponent[]` | 挂载/查询组件 | 🟦 S |
| `GetEntities` | 遍历直接子实体 | 🟩 A |
| `Find*` 查询族 | 多层查找（官方另有 Find 系列方法） | 🟩 A |

## 何时用 / 何时不用

- 用：新项目/新玩法的场景对象组织——这是官方面向未来的模型。
- 不用：维护旧项目里 island 上的 creative_prop 时，两者并用即可，别强行互转。

## 常见坑

- 官方明言"不要直接往 entity 派生类里写代码"——逻辑写在 component 里，entity 只当容器/预制体。
- 组件一旦挂上**不能换父**；要移动就 RemoveFromParent 后重新挂。

## 相关页面

- [component](component.md) —— 行为的载体
- [transform_component](transform_component.md) —— 位置/旋转/缩放
- [agent](../100_Simulation/agent.md) —— agent/player 也继承自 entity
