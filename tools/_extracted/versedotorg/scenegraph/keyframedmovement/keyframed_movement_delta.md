Represents a change in pose and scale over a duration.
|  |  |
| Verse using statement | using { /Verse.org/SceneGraph/KeyframedMovement } |

## Members
This class has data members, but no functions.

### Data
| Data Member Name | Type | Description |
| Transform | transform | Represents a change in the transform relative to the previous keyframe or initial animation position. Translation and Scale are interpreted additively. |
| Duration | float | Duration of this keyframe in seconds. |
| Easing | easing_function | Easing function to use for playback. |
