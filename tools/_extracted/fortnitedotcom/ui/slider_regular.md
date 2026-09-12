Slider with a text value. Displays a slider, its progress bar and value.
|  |  |
| Verse using statement | using { /Fortnite.com/UI } |

## Inheritance Hierarchy
This class is derived from widget.
| Name | Description |
| widget | Base class for all UI elements drawn on the player's screen. |

## Members
This class has both data members and functions.

### Data
| Data Member Name | Type | Description |
| DefaultMaxValue | float | The maximum value that the slider can haver. Used only during initialization of the widget and not modified by SetMaxValue. |
| DefaultMinValue | float | The minimum value that the slider can haver. Used only during initialization of the widget and not modified by SetMinValue. |
| DefaultStepSize | float | The amount to adjust the value by, when using a controller or keyboard. Used only during initialization of the widget and not modified by SetStepSize. |
| DefaultValue | float | The value to display to the user. Used only during initialization of the widget and not modified by SetValue. |

### Functions
| Function Name | Description |
| GetMaxValue | Gets the maximum value of the slider. |
| GetMinValue | Gets the minimum value of the slider. |
| GetParentWidget | Returns the widget's parent widget. Fails if no parent exists, such as if this widget is not in the player_ui or is itself the root widget. |
| GetRootWidget | Returns the widget that added this widget to the player_ui. The root widget will return itself. Fails if this widget is not in the player_ui. |
| GetStepSize | Gets the amount to adjust the value by. |
| GetValue | Gets the value of the slider. |
| GetVisibility | Returns the current widget_visibility state. |
| IsEnabled | true if this widget can be modified interactively by the player. |
| OnValueChanged | Subscribable event that fires when the value of the slider has changed. |
| SetEnabled | Enables or disables whether the player can interact with this widget. |
| SetMaxValue | Sets the maximum value of the slider, will enforce that the sliders maximum value is always larger than or equal to the minimum value. |
| SetMinValue | Sets the minimum value of the slider, will enforce that the sliders maximum value is always larger than or equal to the minimum value. |
| SetStepSize | Sets the amount to adjust the value by, when using a controller or keyboard. |
| SetValue | Sets the value of the slider, will clamp the value to be within the sliders minimum and maximum value. |
| SetVisibility | Shows or hides the widget without removing itself from the containing player_ui. See widget_visibility for details. |
