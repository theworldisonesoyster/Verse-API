Verse path: /UnrealEngine.com/Temporary Module import path: /UnrealEngine.com/Temporary/UI
- UnrealEngine.com
- Temporary
- UI

## Classes and Structs
| Name | Description |
| player_ui | The main interface for adding and removing widgets to a player's UI. |
| widget | Base class for all UI elements drawn on the player's screen. |
| player_ui_slot | widget creation configuration options. |
| widget_message | Parameters for events signalled by a widget. |
| anchors | The anchors of a widget determine its the position and sizing relative to its parent. anchors range from (0.0, 0.0) (left, top) to (1.0, 1.0) (right, bottom). |
| margin | Specifies the gap outside each edge separating a widget from its neighbors. Distance is measured in units where 1.0 unit is the width of a pixel at 1080p resolution. |
| button | Button is a container of a single child widget slot and fires the OnClick event when the button is clicked. |
| button_slot | Slot for button widget. |
| canvas | Canvas is a container widget that allows for arbitrary positioning of widgets in the canvas' slots. |
| canvas_slot | Slot for a canvas widget. |
| color_block | A solid color widget. |
| texture_block | A widget to display a texture. |
| material_block | A widget to display a material. |
| overlay | Overlay is a container consisting of widgets stacked on top of each other. |
| overlay_slot | Slot for an overlay widget |
| stack_box | Stack box is a container of a list of widgets stacked either vertically or horizontally. |
| stack_box_slot | Slot for a stack_box widget |
| text_base | Base widget for text widget. |

## Functions
| Name | Description |
| GetPlayerUI | Returns the player_ui associated with Player. Fails if there is no player_ui associated with Player. |
| MakeCanvasSlot | Make a canvas slot for fixed position widget. If Size is set, then the Offsets is calculated and the SizeToContent is set to false. If Size is not set, then Right and Bottom are set to zero and are not used. The widget size will be automatically calculated. The SizeToContent is set to true. The widget is not anchored and will not move if the parent is resized. The Anchors is set to zero. |

## Enumerations
| Name | Description |
| ui_input_mode | widget input consumption mode. |
| widget_visibility | Used by widget.SetVisibility determine how a widget is shown in the user interface. |
| orientation | Used bywidget orientation modes. |
| horizontal_alignment | widget horizontal alignment mode. |
| vertical_alignment | widget vertical alignment mode. |
| image_tiling | Tiling options values |
| text_justification | Text justification values: Left: Justify the text logically to the left based on current culture. Center: Justify the text in the center. Right: Justify the text logically to the right based on current culture. The Left and Right value will flip when the local culture is right-to-left. |
| text_overflow_policy | Text overflow policy values: Clip: Overflowing text will be clipped. Ellipsis: Overflowing text will be replaced with an ellipsis. |
| text_wrapping_policy | Text wrapping policy values: LineBreak: Allows breaking a line only at line-break iterator for wrapping. PerCharacter: Allows breaking a line after any character for wrapping. |
