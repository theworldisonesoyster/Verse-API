A solid color widget.
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
| DefaultColor | color | The color of the widget. Used only during initialization of the widget and not modified by SetColor. |
| DefaultDesiredSize | vector2 | The size this widget desired to be displayed in. Used only during initialization of the widget and not modified by SetDesiredSize. |
| DefaultOpacity | float | The opacity of the widget. Used only during initialization of the widget and not modified by SetOpacity. |

### Functions
| Function Name | Description |
| GetColor | Gets the widget's color. |
| GetDesiredSize | Gets the size this widget desired to be displayed in. |
| GetOpacity | Gets the widget's opacity. |
| GetParentWidget | Returns the widget's parent widget. Fails if no parent exists, such as if this widget is not in the player_ui or is itself the root widget. |
| GetRootWidget | Returns the widget that added this widget to the player_ui. The root widget will return itself. Fails if this widget is not in the player_ui. |
| GetVisibility | Returns the current widget_visibility state. |
| IsEnabled | true if this widget can be modified interactively by the player. |
| SetColor | Sets the widget's color. |
| SetDesiredSize | Sets the size this widget desired to be displayed in. |
| SetEnabled | Enables or disables whether the player can interact with this widget. |
| SetOpacity | Sets the widgets's opacity. |
| SetVisibility | Shows or hides the widget without removing itself from the containing player_ui. See widget_visibility for details. |
