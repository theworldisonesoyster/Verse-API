Button is a container of a single child widget slot and fires the OnClick event when the button is clicked.
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
| Slot | button_slot | The child widget of the button. Used only during initialization of the widget and not modified by SetSlot. |
| TriggeringInputAction | ??input_action(t) | The UI input action that will trigger the Click event of this button. |

### Functions
| Function Name | Description |
| GetParentWidget | Returns the widget's parent widget. Fails if no parent exists, such as if this widget is not in the player_ui or is itself the root widget. |
| GetRootWidget | Returns the widget that added this widget to the player_ui. The root widget will return itself. Fails if this widget is not in the player_ui. |
| GetVisibility | Returns the current widget_visibility state. |
| HighlightEvent |  |
| IsEnabled | true if this widget can be modified interactively by the player. |
| OnClick | Subscribable event that fires when the button is clicked. |
| SetEnabled | Enables or disables whether the player can interact with this widget. |
| SetVisibility | Shows or hides the widget without removing itself from the containing player_ui. See widget_visibility for details. |
| SetWidget | Sets the child widget slot. |
| UnhighlightEvent |  |
