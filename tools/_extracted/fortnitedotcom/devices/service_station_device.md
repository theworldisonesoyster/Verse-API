A one stop automated refueling and repairing station for your vehicles.
|  |  |
| Verse using statement | using { /Fortnite.com/Devices } |

## Inheritance Hierarchy
This class is derived from the following hierarchy, starting with creative_object:
| Name | Description |
| creative_object | Base class for creative devices and props. |
| creative_device_base | Base class for creative_device. |

## Exposed Interfaces
This class exposes the following interfaces:
| Name | Description |
| healthful | Implemented by Fortnite objects that have health state and can be eliminated. |
| damageable | Implemented by Fortnite objects that can be damaged. |
| enableable | Implemented by classes whose instances can be enabled and disabled. |

## Members
This class has both data members and functions.

### Data
| Data Member Name | Type | Description |
| VehicleEnteredEvent | listenable(payload) | Fires when a vehicle enters the service station, returns the vehicle that entered. |
| VehicleExitedEvent | listenable(payload) | Fires when a vehicle leaves the service station, returns the vehicle that exited. |
| VehicleFuelingBeginEvent | listenable(payload) | Fires on the first tick of a vehicle refueling, returns the refueled vehicle. |
| VehicleFuelingEndEvent | listenable(payload) | Fires when a vehicle is at full fuel, returns the refueled vehicle. |
| VehicleRepairBeginEvent | listenable(payload) | Fires when a vehicle starts repairing, returns the repaired vehicle. |
| VehicleRepairEndEvent | listenable(payload) | Fires when a vehicle is at full health, returns the repaired vehicle. |

### Functions
| Function Name | Description |
| Damage | Damage the damageable object anonymously by Amount. Setting Amount to less than 0 will cause no damage. Use Damage(:damage_args):void when damage is being applied from a known instigator and source. |
| Damage | Damage the damageable object by Args.Amount. Setting Amount to less than 0 will cause no damage. |
| DamagedEvent | Signaled when damage is applied to the damageable object. |
| Disable | Disable this object. |
| Enable | Enable this object. |
| GetGlobalTransform | Gets the global transform of this object. |
| GetHealth | Returns the health state of the object. This value will between 0.0 and GetMaxHealth |
| GetMaxHealth | Returns the maximum health of the object. This value will be between 1.0 and Inf. |
| GetTransform | Returns the transform of the creative_object with units in cm. You must check creative_object.IsValid before calling this if there is a possibility the object has been disposed or destroyed by gameplay. Otherwise a runtime error will result. |
| IsAnyVehicleInside | Check if any vehicle is inside the service station. |
| IsEnabled | Succeeds if the object is enabled, fails if it's disabled. |
| MoveTo | Moves the creative_object to the specified Position and Rotation over the specified time, in seconds. If an animation is currently playing on the creative_object it will be stopped and put into the AnimationNotSet state. |
| MoveTo | Moves the creative_object to the specified Transform over the specified time, in seconds. If an animation is currently playing on the creative_object it will be stopped and put into the AnimationNotSet state. |
| MoveTo | Moves the creative_device to the specified Transform over the specified time, in seconds. If an animation is currently playing on the creative_device it will be stopped and put into the AnimationNotSet state. |
| SetGlobalTransform | Sets the global transform of this object. |
| SetHealth | Sets the health state of the object to Health. Health state will be clamped between 1.0 and GetMaxHealth. Health state cannot be directly set to 0.0. To eliminate healthful objects use the damageable.Damage functions instead. |
| SetMaxHealth | Sets the maximum health state of the object. MaxHealth will be clamped between 1.0 and Inf. Current health state will be scaled up or down based on the scale difference between the old and new MaxHealth state. |
| TeleportTo | Teleports the creative_object to the specified Position and Rotation. |
| TeleportTo | Teleports the creative_object to the specified location defined by Transform, also applies rotation and scale accordingly. |
| TeleportTo | Teleports the creative_device to the specified location defined by Transform, also applies rotation and scale accordingly. |
