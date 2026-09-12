Physics tree that can be chopped down, and damage players, vehicles, creatures, and structures.
|  |  |
| Verse using statement | using { /Fortnite.com/Devices } |

## Inheritance Hierarchy
This class is derived from the following hierarchy, starting with creative_object:
| Name | Description |
| creative_object | Base class for creative devices and props. |
| creative_device_base | Base class for creative_device. |
| prop_spawner_base_device | Base class for devices that spawn a prop object. |
| physics_object_base_device | Base class for various physics-based gameplay elements (e.g. boulders/trees). |

## Members
This class has both data members and functions.

### Data
| Data Member Name | Type | Description |
| LogDestroyedEvent | listenable(payload) | Signaled when the log created by a tree is destroyed. |
| StumpDestroyedEvent | listenable(payload) | Signaled when the stump created by a tree is destroyed. |
| TreeKnockedDownEvent | listenable(payload) | Signaled when a tree has taken enough damage to be knocked down. |
| TreeSpawnedEvent | listenable(payload) | Signaled when a tree is spawned. |

### Functions
| Function Name | Description |
| DestroyAllSpawnedObjects | Destroys all props spawned from this device. |
| DestroyLog | Destroys the current log. |
| DestroyStump | Destroys the current stump. |
| Disable | Disables this device. |
| Enable | Enables this device. |
| GetGlobalTransform | Gets the global transform of this object. |
| GetTransform | Returns the transform of the creative_object with units in cm. You must check creative_object.IsValid before calling this if there is a possibility the object has been disposed or destroyed by gameplay. Otherwise a runtime error will result. |
| MoveTo | Moves the creative_object to the specified Position and Rotation over the specified time, in seconds. If an animation is currently playing on the creative_object it will be stopped and put into the AnimationNotSet state. |
| MoveTo | Moves the creative_object to the specified Transform over the specified time, in seconds. If an animation is currently playing on the creative_object it will be stopped and put into the AnimationNotSet state. |
| MoveTo | Moves the creative_device to the specified Transform over the specified time, in seconds. If an animation is currently playing on the creative_device it will be stopped and put into the AnimationNotSet state. |
| ReleaseLog | Releases the log from the tree, if there is one. |
| SetGlobalTransform | Sets the global transform of this object. |
| SpawnObject | Spawns the prop associated with this device. |
| TeleportTo | Teleports the creative_object to the specified Position and Rotation. |
| TeleportTo | Teleports the creative_object to the specified location defined by Transform, also applies rotation and scale accordingly. |
| TeleportTo | Teleports the creative_device to the specified location defined by Transform, also applies rotation and scale accordingly. |
