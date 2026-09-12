The main interface for adding and removing widgets to a player's UI.
|  |  |
| Verse using statement | using { /UnrealEngine.com/Temporary/UI } |

## Members
This class has functions, but no data members.

### Functions
| Function Name | Description |
| AddWidget | Adds Widget to this player_ui using default player_ui_slot configuration options. |
| AddWidget | Adds Widget to this player_ui using Slot for configuration options. |
| RemoveWidget | Removes Widget from this player_ui. |
| SetFocus | Sets the user's focus on this Widget. The target Widgetmust be focusable, otherwise this has no effect. If SetFocus is called before AddWidget, the widget will be focused after AddWidget is called, unless a SetFocus is called on a different widget by the time AddWidget is called. |
