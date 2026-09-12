Base class for all UI elements drawn on the player's screen.
|  |  |
| Verse using statement | using { /UnrealEngine.com/Temporary/UI } |

## Members
This class has functions, but no data members.

### Functions
| Function Name | Description |
| SetVisibility | Shows or hides the widget without removing itself from the containing player_ui. See widget_visibility for details. |
| GetVisibility | Returns the current widget_visibility state. |
| SetEnabled | Enables or disables whether the player can interact with this widget. |
| IsEnabled | true if this widget can be modified interactively by the player. |
| GetParentWidget | Returns the widget's parent widget. Fails if no parent exists, such as if this widget is not in the player_ui or is itself the root widget. |
| GetRootWidget | Returns the widget that added this widget to the player_ui. The root widget will return itself. Fails if this widget is not in the player_ui. |
