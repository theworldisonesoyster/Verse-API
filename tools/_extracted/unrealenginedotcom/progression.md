Module import path: /UnrealEngine.com/Progression
- UnrealEngine.com
- Progression

## Classes and Structs
| Name | Description |
| quest_category | A category in the quest UI. |
| basic_quest | Standard quest that follows the "do x, get y" paradigm. Auto-completion: when Objective.IsComplete() succeeds, calls Complete() automatically. Auto-rewarding: on completion, rewards are granted to eligible participants via GetRecipients() then GrantReward(). |
| quest_objective | Abstract base class for all quest objectives. |
| grant_quest_reward_error | Returned when a reward cannot be granted. |
| quest_reward | Abstract base class for all quest rewards. |
| entitlement_quest_reward | Grants an entitlement to each eligible participant. |
| progress_quest_objective | Tracks numeric progress toward a required count. Complete when Progress >= RequiredCount. |

## Interfaces
| Name | Description |
| has_quest_presentation | Implement on a quest class to customize how it displays in the quest UI. |
