An easing function combined with a relative time window
|  |  |
| Verse using statement | using { /Verse.org/SceneGraph } |

## Members
This struct has data members, but no functions.

### Data
| Data Member Name | Type | Description |
| Easing | (float):float | Easing function to apply |
| Duration | float | Duration of the easing window in seconds |
| Offset | float | Offset of the easing window in seconds The offset allows the window to be moved later or earlier relative to the easing modifier’s internal timeline. For example, moving the ease-in window later (ie +Offset) would cause the blend to happen later - ie delay it. For -ve offsets to ease-in and +ve offsets to ease-out, this has the effect of allowing ‘frozen’ states of targets to be observed (for time-varying targets). |
