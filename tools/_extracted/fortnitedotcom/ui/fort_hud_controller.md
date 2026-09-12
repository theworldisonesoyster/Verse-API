A HUD controller that allows for showing and hiding of HUD elements.
|  |  |
| Verse using statement | using { /Fortnite.com/UI } |

## Members
This interface has functions, but no data members.

### Functions
| Function Name | Description |
| ShowElements | Shows a set of HUD elements for every player. Note: This can be overridden by rules set by 'ForPlayer' functions since player specific rules are prioritized over general rules. |
| HideElements | Hides a set of HUD elements for every player. Note: This can be overridden by rules set by 'ForPlayer' functions since player specific rules are prioritized over general rules. |
| ResetElementVisibility | Resets the visibility for a set of HUD elements for every player. Note: This will not clear player specific rules set by the 'ForPlayer' functions which can only be reset by calling 'ResetElementsForPlayer'. |
| ShowElementsForPlayer | Shows a set of HUD elements for a single player. Note: This overrides general rules set by non-player functions for the given elements. Call 'ResetElementsForPlayer' in order to return the player to general behavior |
| HideElementsForPlayer | Hides a set of HUD elements for a single player. Note: This overrides general rules set by non-player functions for the given elements. Call 'ResetElementsForPlayer' in order to return the player to general behavior |
| ResetElementsForPlayer | Resets the player-specific visibility rules of a set of HUD elements for a single player. Note: This will not reset rules that have been set by means other than the 'PerPlayer' functions. |
