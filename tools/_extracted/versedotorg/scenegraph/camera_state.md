|  |  |
| Verse using statement | using { /Verse.org/SceneGraph } |

## Members
This class has data members, but no functions.

### Data
| Data Member Name | Type | Description |
| RenderLocation | vector3 | Render location of the camera. This render location can be modified by camera directions (like camera shakes), without modifying the physical location of any camera entity |
| RenderRotation | rotation | Render rotation of the camera. This render rotation can be modified by camera directions (like camera shakes), without modifying the physical location of any camera entity |
| OrthographicProjectionWidth | float | Determines how wide the camera projects in orthographic mode, in centimeters - Used only if projection mode is orthographic |
| Body | camera_body | Physical camera body settings |
| Lens | camera_lens | Physical camera lens settings |
| ProjectionMode | camera_projection_mode | Projection mode - perspective or orthographic |
| PhysicalCameraWeight | float | How much to apply physical camera settings between 0.0 and 1.0 |
| NearClippingPlaneDistance | float |  |
| FarClippingPlaneDistance | float |  |
