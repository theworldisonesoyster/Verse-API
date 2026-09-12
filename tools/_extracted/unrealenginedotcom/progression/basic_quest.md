Standard quest that follows the "do x, get y" paradigm. Auto-completion: when Objective.IsComplete() succeeds, calls Complete() automatically. Auto-rewarding: on completion, rewards are granted to eligible participants via GetRecipients() then GrantReward().
|  |  |
| Verse using statement | using { /UnrealEngine.com/Progression } |

## Inheritance Hierarchy
This class is derived from quest.
| Name | Description |
| quest | A completable goal. Call Complete() to mark the quest as done and fire CompleteEvent. |

## Exposed Interfaces
This class exposes the following interfaces:
| Name | Description |
| has_icon | Interface that provides an icon. |
| has_description | Interface that provides descriptive names or text. |

## Members
This class has both data members and functions.

### Data
| Data Member Name | Type | Description |
| AbandonEvent | unknown | Signaled when a participant abandons this quest. |
| CompleteEvent | unknown | Signaled when this quest completes. |
| JoinEvent | unknown | Signaled when a participant joins this quest. |
| Objective | ?quest_objective | Progression model for the quest. |
| Rewards | ?[]quest_reward | Rewards granted to eligible participants on completion. |

### Functions
| Function Name | Description |
| Complete | Marks this quest as completed. Fires CompleteEvent. Idempotent — no-op if already completed. |
| IsComplete | Succeeds if this quest is completed. |
| SetObjective | Replaces the progression model on a live quest. Auto-completes if the new objective is already completed. |
