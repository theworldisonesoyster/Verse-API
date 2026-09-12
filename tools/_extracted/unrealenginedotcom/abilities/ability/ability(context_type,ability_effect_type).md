Lives in the scene graph and is the high level description of an ability. Knows if an ability can run, cooldowns, distance and targeting requirements etc...
|  |  |
| Verse using statement | using { /UnrealEngine.com/Abilities } |

## Exposed Interfaces
This class exposes the following interfaces:
| Name | Description |
| has_icon | Interface that provides an icon. |

## Members
This class has both data members and functions.

### Data
| Data Member Name | Type | Description |
| BeginUseEvent | listenable(payload) |  |
| EndUseEvent | listenable(payload) |  |
| ActiveEffects | ?[] |  |
| Icon | ?texture |  |

### Functions
| Function Name | Description |
| Use |  |
| CanUse |  |
| MakeContext |  |
| MakeAbility |  |
