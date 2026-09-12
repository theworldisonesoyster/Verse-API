Used to configuration and spawn items that players can pick up and use.
|  |  |
| Verse using statement | using { /Fortnite.com/Devices } |

## Inheritance Hierarchy
This class is derived from the following hierarchy, starting with creative_object:
| Name | Description |
| creative_object | Base class for creative devices and props. |
| creative_device_base | Base class for creative_device. |
| base_item_spawner_device | Base class for devices that spawn items. |

## Members
This class has both data members and functions.

### Data
| Data Member Name | Type | Description |
| ItemPickedUpEvent | listenable(payload) | Signaled when an agent picks up the spawned item. Sends the agent that picked up the item. |

### Functions
| Function Name | Description |
| CycleToNextItem | Cycles device to next configured item. |
| Disable | Disables this device. |
| Enable | Enables this device. |
| GetEnableRespawnTimer | Returns device Respawn Item on Timer option (see SetTimeBetweenSpawns) |
| GetGlobalTransform | Gets the global transform of this object. |
| GetTimeBetweenSpawns | Returns the Time Between Spawns (in seconds) after an item is collected before the next is spawned, if this device has Respawn Item on Timer enabled (see SetEnableRespawnTimer) |
| GetTransform | Returns the transform of the creative_object with units in cm. You must check creative_object.IsValid before calling this if there is a possibility the object has been disposed or destroyed by gameplay. Otherwise a runtime error will result. |
| MoveTo | Moves the creative_object to the specified Position and Rotation over the specified time, in seconds. If an animation is currently playing on the creative_object it will be stopped and put into the AnimationNotSet state. |
| MoveTo | Moves the creative_object to the specified Transform over the specified time, in seconds. If an animation is currently playing on the creative_object it will be stopped and put into the AnimationNotSet state. |
| MoveTo | Moves the creative_device to the specified Transform over the specified time, in seconds. If an animation is currently playing on the creative_device it will be stopped and put into the AnimationNotSet state. |
| SetEnableRespawnTimer | Sets device Respawn Item on Timer option (see SetTimeBetweenSpawns) |
| SetGlobalTransform | Sets the global transform of this object. |
| SetTimeBetweenSpawns | Sets the Time Between Spawns (in seconds) after an item is collected before the next is spawned, if this device has Respawn Item on Timer enabled (see SetEnableRespawnTimer) |
| SpawnItem | Spawns the current item. |
| TeleportTo | Teleports the creative_object to the specified Position and Rotation. |
| TeleportTo | Teleports the creative_object to the specified location defined by Transform, also applies rotation and scale accordingly. |
| TeleportTo | Teleports the creative_device to the specified location defined by Transform, also applies rotation and scale accordingly. |
