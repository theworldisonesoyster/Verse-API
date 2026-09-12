Abstract base class for all quest rewards.
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
| GrantEvent | listenable(payload) | Signaled after this reward has been granted to recipients. |

### Functions
| Function Name | Description |
| GetRecipients | Determines which participants should receive this reward. Override to customize recipient selection. Default: all participants where Info.Receives = true. |
| GrantReward | Grants this reward to the eligible participants. |
