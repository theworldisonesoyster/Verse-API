Collision Volumes represent the collision shapes of meshes. They can be detected by Overlap and Sweep queries and generate collisions in the physics simulation.
|  |  |
| Verse using statement | using { /Verse.org/SceneGraph } |

## Members
This class has both data members and functions.

### Data
| Data Member Name | Type | Description |
| Collidable | ?logic | Enable/disable collision on this volume. |
| Queryable | ?logic | Enable/disable spatial queries against this volume. |

### Functions
| Function Name | Description |
| GetLocalTransform | Get the transform of this volume in the space of its owner (usually a component on an entity) |
| SetLocalTransform | Set the transform of this volume in the space of its owner (usually a component on an entity) |
