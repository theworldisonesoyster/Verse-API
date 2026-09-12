Canvas is a container widget that allows for arbitrary positioning of widgets in the canvas' slots.
|  |  |
| Verse using statement | using { /UnrealEngine.com/Temporary/UI } |

## Inheritance Hierarchy
This class is derived from widget.
| Name | Description |
| widget | Base class for all UI elements drawn on the player's screen. |

## Members
This class has both data members and functions.

### Data
| Data Member Name | Type | Description |
| Slots | []canvas_slot | The child widgets of the canvas. Used only during initialization of the widget and not modified by Add/RemoveWidget. |

### Functions
| Function Name | Description |
| AddWidget | Adds a new child slot to the canvas. |
| GetParentWidget | Returns the widget's parent widget. Fails if no parent exists, such as if this widget is not in the player_ui or is itself the root widget. |
| GetRootWidget | Returns the widget that added this widget to the player_ui. The root widget will return itself. Fails if this widget is not in the player_ui. |
| GetVisibility | Returns the current widget_visibility state. |
| IsEnabled | true if this widget can be modified interactively by the player. |
| RemoveWidget | Removes a slot containing the given widget. |
| SetEnabled | Enables or disables whether the player can interact with this widget. |
| SetVisibility | Shows or hides the widget without removing itself from the containing player_ui. See widget_visibility for details. |
