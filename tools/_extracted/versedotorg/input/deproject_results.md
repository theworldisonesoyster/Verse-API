Holds the world-space ray produced by deprojecting a viewport coordinate.
|  |  |
| Verse using statement | using { /Verse.org/Input } |

## Members
This struct has data members, but no functions.

### Data
| Data Member Name | Type | Description |
| Origin | vector3 | World space position of the camera (the ray's origin). This is the camera eye point, not the near plane — a trace starting here may intersect geometry between the camera and the near plane that is not visible on screen. Use collision filtering to ignore the player pawn, or advance the start point along Direction past the near clip distance. |
| Direction | vector3 | Normalized world space direction vector of the ray, pointing from the camera through the given viewport coordinate into the scene. |
