Prefab to provide a central location for handling desired ability and gameplay logic.
|  |  |
| Verse using statement | using { /UnrealEngine.com/Abilities } |

## Inheritance Hierarchy
This class is derived from entity.
| Name | Description |
| entity | Entities are the base object in the SceneGraph. Objects in experiences are constructed of one or more entities. Entities are hierarchical. You can query your parent using GetParent and add child entities using AddEntities. Behavior is added to entities through components. You can add new components using AddComponents. The structure and content of entities is dynamic and be changed at any time through your experience . Deriving from entity In the SceneGraph system a class that derives from entity is also known as a prefab. Prefabs are useful when you want to spawn/re-use a collection of entities and components many times within your game. Primarily prefabs are authored through the editor, with their Verse classes generated as part of the build into the projects Assets.digest.verse file. While you can create base prefabs for common game object types like a vehicle or character, we highly recommended that you do not add code directly to the entity class, and instead keep logic in components. Keeping logic and data in components allows you to restructure your prefabs throughout production of your experience, without needing to massively refactor your class structure. |

## Members
This class has both data members and functions.

### Data
| Data Member Name | Type | Description |
| AbilityComponent | ability_effect_component |  |

### Functions
| Function Name | Description |
| AddComponents | Adds the provided components to the entity. If a component is not allowed to be added to this entity it is skipped. Note: When called during the AddedToScene or BeginSimulation phase, it will make sure the added component has achieved the corresponding phase. Components are added following these rules: All components are added to the entity child list. All components have OnAddedToScene called (if this entity is in the scene). All components have OnBeginSimulation called (if this entity is simulating). |
| AddEntities | Adds the provided entities as children of this entity. If child entity already has a parent, removes the entity from its current parent and adds it to the new one. Added child entities will move through their lifetime methods until they match the state of the new parent. |
| AddTag | Adds a tag instance to this entity. Returns a tag_key that is uniquely associated with the added instance. |
| ContainsAllTags | Fails if at least one type in tag_types cannot be found in this container, succeeds otherwise. Note that this means that if tag_types is empty this call succeeds. |
| ContainsAnyTag | Succeeds if at least of the types in tag_types is found in this container, fails otherwise. Note that this means that if tag_types is empty this call fails. |
| ContainsTag | Succeeds if at least one tag of type tag_type is found in this container, fails otherwise. |
| GetComponent | Succeeds and returns the child component of type component_type if it exists and is accessible from the calling context. Note: When called during the AddedToScene or BeginSimulation phase, it will make sure the returned component has achieved the corresponding phase. Fails if no component of component_type exists or can be accessed. |
| GetComponents | Returns the child components belonging to this entity which are accessible from the calling context. |
| GetEntities | Returns the child entities belonging to this entity which are accessible from the calling context. This method only gets the direct entity children. To query multiple levels down the entity structure use the Find* query methods instead. |
| GetParent | Returns the parent entity of this entity. The parent entity controls the lifetime of its child entities and components. When an entity is removed from the scene, all its child entities and components will be removed as well. Method fails if there is currently no parent entity. |
| RemoveAllTags | Removes all tag instances of type tag_type, succeeds if at least one instance was removed, fails otherwise. |
| RemoveAllTagsExcept | Removes all tag instances that are not of type tag_type, succeeds if at least one instance was removed, fails otherwise. |
| RemoveAllTagsExcept | Removes all tag instances that are not of any of the types in tag_types, succeeds if at least one instance was removed, fails otherwise. |
| RemoveFromParent | Removes this entity from its parent. This is used to remove entities from the scene. Components on this entity and its children will run through OnEndSimulation -> OnRemovingFromScene. Entity can be added back later by using NewParent.AddEntities. |
| RemoveTag | Removes the tag instance associated with the tag_key, succeeds if an instance was removed, fails otherwise. |
| SendDown | Send a scene event to this entity and then down the hierarchy. First, SendDown/OnReceive will be invoked on each component on this entity. Next, SendDown will be invoked on each child entity. Consuming the event at any point will halt propagation. Returns true if any participant consumed the event. |
| SendUp | Send a scene event to this entity and then up the hierarchy. First, SendDown/OnReceive will be invoked on each component on this entity. Next, SendUp will be invoked on this entity's parent. Consuming the event at any point will halt propagation. Returns true if any participant consumed the event. |
