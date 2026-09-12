Specialized vehicle_spawner_device that allows a pickup truck to be configured and spawned.
|  |  |
| Verse using statement | using { /Fortnite.com/Devices } |

## Inheritance Hierarchy
This class is derived from the following hierarchy, starting with creative_object:
| Name | Description |
| creative_object | Base class for creative devices and props. |
| creative_device_base | Base class for creative_device. |
| vehicle_spawner_device | Base class for various specialized vehicle spawners which allow specific vehicle types to be spawned and configured with specialized options. |

## Members
This class has both data members and functions.

### Data
| Data Member Name | Type | Description |
| AgentEntersVehicleEvent | listenable(payload) | Signaled when an agent enters the vehicle. Sends the agent that entered the vehicle. |
| AgentExitsVehicleEvent | listenable(payload) | Signaled when an agent exits the vehicle. Sends the agent that exited the vehicle. |
| DestroyedEvent | listenable(payload) | Signaled when a vehicle is destroyed. |
| SpawnedEvent | listenable(payload) | Signaled when a vehicle is spawned or respawned by this device. Sends the fort_vehicle who was spawned. |
| Vehicle | ??fort_vehicle | The fort_vehicle currently associated with this spawner, if one exists. |
| VehicleDestroyedEvent | listenable(payload) | Signaled when a vehicle is destroyed. Deprecated, use DestroyedEvent instead. |
| VehicleSpawnedEvent | listenable(payload) | Signaled when a vehicle is spawned or respawned by this device. Deprecated, use SpawnedEvent instead. |

### Functions
| Function Name | Description |
| AssignDriver | Sets agent as the vehicle's driver. |
| DestroyVehicle | Destroys the vehicle if it exists. |
| Disable | Disables this device. |
| Enable | Enables this device. |
| GetGlobalTransform | Gets the global transform of this object. |
| GetTransform | Returns the transform of the creative_object with units in cm. You must check creative_object.IsValid before calling this if there is a possibility the object has been disposed or destroyed by gameplay. Otherwise a runtime error will result. |
| MoveTo | Moves the creative_object to the specified Position and Rotation over the specified time, in seconds. If an animation is currently playing on the creative_object it will be stopped and put into the AnimationNotSet state. |
| MoveTo | Moves the creative_object to the specified Transform over the specified time, in seconds. If an animation is currently playing on the creative_object it will be stopped and put into the AnimationNotSet state. |
| MoveTo | Moves the creative_device to the specified Transform over the specified time, in seconds. If an animation is currently playing on the creative_device it will be stopped and put into the AnimationNotSet state. |
| RespawnVehicle | Spawns a new vehicle. The previous vehicle will be destroyed before a new vehicle spawns. |
| SetGlobalTransform | Sets the global transform of this object. |
| TeleportTo | Teleports the creative_object to the specified Position and Rotation. |
| TeleportTo | Teleports the creative_object to the specified location defined by Transform, also applies rotation and scale accordingly. |
| TeleportTo | Teleports the creative_device to the specified location defined by Transform, also applies rotation and scale accordingly. |
