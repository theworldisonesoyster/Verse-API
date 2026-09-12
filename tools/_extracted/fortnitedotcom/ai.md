Verse path: /Fortnite.com Module import path: /Fortnite.com/AI
- Fortnite.com
- AI movement_types

## Classes and Structs
| Name | Description |
| equipped_sidekick_component | Component to manage functionality specifically for an agent's equipped Sidekick. |
| spark_mode_component | component to manage an entity that supports a Spark mode. Spark mode will transform the entity into a floating spark. The entity will enter spark mode whenever it enters impassable terrain or to reduce visual clutter. |
| guard_actions_component | Fortnite Guards AI actions management |
| guard_awareness_component | Fortnite Guard perception management |
| navigation_target |  |
| npc_actions_component | Fortnite NPC AI actions management |
| npc_awareness_component | Fortnite NPC perception management |
| npc_behavior | Inherit from this to create a custom NPC behavior. The npc_behavior can be defined for a character in a CharacterDefinition asset, or in a npc_spawner_device. |
| npc_target_info | Information about a perceived target. |
| sidekick_component | Component to manage functionality shared by all Sidekick types. |
| npc_sidekick_component | Component to manage functionality specifically for an NPC Sidekick. |

## Interfaces
| Name | Description |
| focus_interface |  |
| fort_leashable |  |
| navigatable |  |

## Functions
| Name | Description |
| MakeNavigationTarget | Generate a navigation_target from any position. |
| MakeNavigationTarget | Generate a navigation_target from any position. |
| MakeNavigationTarget | Generate a navigation_target from an agent. |

## Enumerations
| Name | Description |
| ai_action_error_type | Result of a failed AI action |
| navigation_result | Result of a navigation request |
| navigation_action_error_type |  |
| navigation_action_success_type |  |
| movement_type |  |
| guard_alert_level | The different alert levels of a Fortnite Guard. |
| sidekick_mood | Sidekicks have a mood that modifies their animations to suit that mood. This is the list of currently supported moods. |
| sidekick_reaction | The set of available reactions that can be played on the Sidekick |
