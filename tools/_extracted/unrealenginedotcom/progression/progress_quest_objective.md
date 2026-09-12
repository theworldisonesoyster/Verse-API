Tracks numeric progress toward a required count. Complete when Progress >= RequiredCount.
|  |  |
| Verse using statement | using { /UnrealEngine.com/Progression } |

## Inheritance Hierarchy
This class is derived from quest_objective.
| Name | Description |
| quest_objective | Abstract base class for all quest objectives. |

## Members
This class has both data members and functions.

### Data
| Data Member Name | Type | Description |
| CompleteEvent | listenable(payload) | Signaled when this objective is considered complete. |
| Progress | ?float | Current progress toward RequiredCount. |
| ProgressEvent | listenable(payload) | Signaled when this objective's progress changes. Payload: this objective. |
| RequiredCount | ?float | Target count for completion. |

### Functions
| Function Name | Description |
| GetContributors | Determines which participants can contribute to this objective. Override to customize contributor selection. Default: all participants where Info.Contributes = true. |
| GetProgress | Returns progress in "X / Y" format. |
| GetProgress | Returns a progress message (e.g. "3 / 10"). |
| IsComplete | Succeeds if Progress >= RequiredCount. |
| IsComplete | Succeeds if this objective is currently complete. |
| SetProgress | Sets current progress. Clamped to [0, RequiredCount]. |
| SetRequiredCount | Sets the target count. Clamped to [1, MaxFloat]. |
| SignalProgressEvent | Signals ProgressEvent. Call from a subclass to notify progress subscribers. |
