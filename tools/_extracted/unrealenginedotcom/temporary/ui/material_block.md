A widget to display a material.
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
| DefaultDesiredSize | vector2 | The size this widget desired to be displayed in. Used only during initialization of the widget and not modified by SetDesiredSize. |
| DefaultImage | material | The image to render. Used only during initialization of the widget and not modified by SetImage. |
| DefaultTint | color | Tinting applied to the image. Used only during initialization of the widget and not modified by SetTint. |

### Functions
| Function Name | Description |
| GetDesiredSize | Gets the size this widget desired to be displayed in. |
| GetImage | Gets the image to render. |
| GetParentWidget | Returns the widget's parent widget. Fails if no parent exists, such as if this widget is not in the player_ui or is itself the root widget. |
| GetRootWidget | Returns the widget that added this widget to the player_ui. The root widget will return itself. Fails if this widget is not in the player_ui. |
| GetTint | Gets the tint applied to the image. |
| GetVisibility | Returns the current widget_visibility state. |
| IsEnabled | true if this widget can be modified interactively by the player. |
| SetDesiredSize | Sets the size this widget desired to be displayed in. |
| SetEnabled | Enables or disables whether the player can interact with this widget. |
| SetImage | Sets the image to render. |
| SetTint | Sets the tint applied to the image. |
| SetVisibility | Shows or hides the widget without removing itself from the containing player_ui. See widget_visibility for details. |
