Abstract base class for all quest objectives.
|  |  |
| Verse using statement | using { /UnrealEngine.com/Progression } |

## Exposed Interfaces
This class exposes the following interfaces:
| Name | Description |
| has_icon | Interface that provides an icon. |
| has_description | Interface that provides descriptive names or text. |

## Members
This class has both data members and functions.

### Data
| Data Member Name | Type | Description |
| CompleteEvent | listenable(payload) | Signaled when this objective is considered complete. |
| ProgressEvent | listenable(payload) | Signaled when this objective's progress changes. Payload: this objective. |

### Functions
| Function Name | Description |
| GetProgress | Returns a progress message (e.g. "3 / 10"). |
| GetContributors | Determines which participants can contribute to this objective. Override to customize contributor selection. Default: all participants where Info.Contributes = true. |
| IsComplete | Succeeds if this objective is currently complete. |
| SignalProgressEvent | Signals ProgressEvent. Call from a subclass to notify progress subscribers. |
