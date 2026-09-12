- UnrealEngine.com
- Abilities

## Classes and Structs
| Name | Description |
| ability_context | Data passed on activation of an ability. Holds who fired, who helped, and what got hit. Subclass to provide specific context for custom ability effects |
| ability_effect | Prefab to provide a central location for handling desired ability and gameplay logic. |
| ability(context_type,ability_effect_type) | Lives in the scene graph and is the high level description of an ability. Knows if an ability can run, cooldowns, distance and targeting requirements etc... |
| cancel_reason | Lightweight tag explaining why an effect ended. |
| ability_ended |  |
| ability_removed_from_scene |  |
| ability_effect_component | Guaranteed Ability component on Ability prefab entities. Handles Ability lifecycle. |

## Functions
| Name | Description |
| MakeAbilityEffectComponent |  |
| ability | Lives in the scene graph and is the high level description of an ability. Knows if an ability can run, cooldowns, distance and targeting requirements etc... |
