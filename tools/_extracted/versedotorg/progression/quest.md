A completable goal. Call Complete() to mark the quest as done and fire CompleteEvent.
|  |  |
| Verse using statement | using { /Verse.org/Progression } |

## Members
This class has both data members and functions.

### Data
| Data Member Name | Type | Description |
| JoinEvent | unknown | Signaled when a participant joins this quest. |
| AbandonEvent | unknown | Signaled when a participant abandons this quest. |
| CompleteEvent | unknown | Signaled when this quest completes. |

### Functions
| Function Name | Description |
| Complete | Marks this quest as completed. Fires CompleteEvent. Idempotent — no-op if already completed. |
| IsComplete | Succeeds if this quest is completed. |
