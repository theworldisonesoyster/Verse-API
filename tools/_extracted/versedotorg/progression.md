Module import path: /Verse.org/Progression
- Verse.org
- Progression

## Classes and Structs
| Name | Description |
| quest_participant_info | Describes how a participant relates to a quest. |
| quest_membership | Record binding a quest to a participant with participation info. |
| join_quest_error | Returned when a participant cannot join a quest. |
| abandon_quest_error | Returned when a participant cannot abandon a quest. |
| quest | A completable goal. Call Complete() to mark the quest as done and fire CompleteEvent. |
| quest_collection | The source of truth for quest participation. |
| quest_participant | Abstract base class for quest participants. |
| agent_quest_participant | A quest participant backed by an agent (player, NPC, AI, etc.). |
