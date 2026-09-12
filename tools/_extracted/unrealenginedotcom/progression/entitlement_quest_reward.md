Grants an entitlement to each eligible participant.
|  |  |
| Verse using statement | using { /UnrealEngine.com/Progression } |

## Inheritance Hierarchy
This class is derived from quest_reward.
| Name | Description |
| quest_reward | Abstract base class for all quest rewards. |

## Members
This class has both data members and functions.

### Data
| Data Member Name | Type | Description |
| Entitlement | ?concrete_subtype(entitlement) | The entitlement type to grant. |
| GrantEvent | listenable(payload) | Signaled after this reward has been granted to recipients. |
| Quantity | ?int | Quantity per participant. |

### Functions
| Function Name | Description |
| GetRecipients | Determines which participants should receive this reward. Override to customize recipient selection. Default: all participants where Info.Receives = true. |
| GrantReward | Iterates EligibleParticipants, resolves each participant's agent as a player, and grants the entitlement via the platform entitlement service. |
| GrantReward | Grants this reward to the eligible participants. |
