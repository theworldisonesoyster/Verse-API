Base widget for text widget.
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
| AutoWrap | ?logic | Whether the text should be automatically wrapped. |
| DefaultJustification | text_justification | The justification to display to the user. Used only during initialization of the widget and not modified by SetJustification. |
| DefaultOverflowPolicy | text_overflow_policy | The policy that determine what happens when the text is longer than its allowed length. Used only during initialization of the widget and not modified by SetOverflowPolicy. |
| DefaultText | message | The text to display to the user. Used only during initialization of the widget and not modified by SetText. |
| DefaultTextColor | color | The color of the displayed text. Used only during initialization of the widget and not modified by SetTextColor. |
| DefaultTextOpacity | float | The opacity of the displayed text. Used only during initialization of the widget and not modified by SetTextOpacity. |
| DefaultTextSize | float | The size of the displayed text. Used only during initialization of the widget and not modified by SetTextSize. |
| WrappingPolicy | ?text_wrapping_policy | The wrapping policy to determine where the line can be broken. |
| WrapWidth | ?float | Whether text wraps onto a new line when it's length exceeds this width; if this value is zero or negative, no wrapping occurs. |

### Functions
| Function Name | Description |
| GetJustification | Gets the text justification in the widget. |
| GetOverflowPolicy | Gets the policy that determine what happens when the text is longer than its allowed length. |
| GetParentWidget | Returns the widget's parent widget. Fails if no parent exists, such as if this widget is not in the player_ui or is itself the root widget. |
| GetRootWidget | Returns the widget that added this widget to the player_ui. The root widget will return itself. Fails if this widget is not in the player_ui. |
| GetText | Gets the text currently in the widget. |
| GetTextColor | Gets the color of the displayed text. |
| GetTextOpacity | Gets the opacity of the displayed text. |
| GetTextSize | Gets the size of the displayed text. |
| GetVisibility | Returns the current widget_visibility state. |
| IsEnabled | true if this widget can be modified interactively by the player. |
| SetEnabled | Enables or disables whether the player can interact with this widget. |
| SetJustification | Sets the text justification in the widget. |
| SetOverflowPolicy | Sets the policy that determine what happens when the text is longer than its allowed length. |
| SetText | Sets the text displayed in the widget. |
| SetTextColor | Sets the color of the displayed text. |
| SetTextOpacity | Sets the opacity of the displayed text. |
| SetTextSize | Sets the size of the displayed text. |
| SetVisibility | Shows or hides the widget without removing itself from the containing player_ui. See widget_visibility for details. |
