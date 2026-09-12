Use to create a flaming hoop that accelerates and applies nitro to players and vehicles.
|  |  |
| Verse using statement | using { /Fortnite.com/Devices } |

## Inheritance Hierarchy
This class is derived from the following hierarchy, starting with creative_object:
| Name | Description |
| creative_object | Base class for creative devices and props. |
| creative_device_base | Base class for creative_device. |

## Members
This class has both data members and functions.

### Data
| Data Member Name | Type | Description |
| CooldownStartEvent | listenable(payload) | Triggers when the device enters the cooldown state, becoming disabled. This is not triggered by manually calling Disable. |
| EnabledEvent | listenable(payload) | Triggers when the device becomes enabled after being disabled, potentially through the cooldown state. |
| PlayerTriggeredEvent | listenable(payload) | Triggers when a player triggers the device. Sends the triggering agent. |
| VehicleTriggeredEvent | listenable(payload) | Triggers when a vehicle triggers the device. Sends the driver as the triggering agent. If the vehicle has no driver then false is returned. |

### Functions
| Function Name | Description |
| AllowCooldown | Allow the device to enter the cooldown state after a player or vehicle triggers it. |
| Disable | Disable the device. This causes the device to enter the cooldown state until the device is re-enabled by Enable, DisallowCooldown, or Enable on Phase. |
| DisallowCooldown | Prevent the device from entering the cooldown state after use. Until AllowCooldown is called, triggering the device will not begin cooldown. If the device is currently in the cooldown state, this ends the cooldown state and re-enables the device. |
| Enable | Enable the device. If the device is currently in the cooldown state, this also ends the cooldown state. |
| GetCooldownDelay | Return the duration of the cooldown delay in seconds. This is the delay between triggering a cooldown and entering the cooldown phase. |
| GetDefaultCooldownDuration | Return the default duration of the cooldown state in seconds. |
| GetGlobalTransform | Gets the global transform of this object. |
| GetTransform | Returns the transform of the creative_object with units in cm. You must check creative_object.IsValid before calling this if there is a possibility the object has been disposed or destroyed by gameplay. Otherwise a runtime error will result. |
| IsEnabled | Succeeds if the device is currently enabled. The device is not enabled if it is in the cooldown state, or has otherwise been manually disabled. |
| MoveTo | Moves the creative_object to the specified Position and Rotation over the specified time, in seconds. If an animation is currently playing on the creative_object it will be stopped and put into the AnimationNotSet state. |
| MoveTo | Moves the creative_object to the specified Transform over the specified time, in seconds. If an animation is currently playing on the creative_object it will be stopped and put into the AnimationNotSet state. |
| MoveTo | Moves the creative_device to the specified Transform over the specified time, in seconds. If an animation is currently playing on the creative_device it will be stopped and put into the AnimationNotSet state. |
| SetCooldownDelay | Set the duration of the cooldown delay to Seconds. This is the delay between triggering a cooldown and entering the cooldown phase. The cooldown delay does not apply to cooldowns triggered by StartCooldown or Disable. Seconds is clamped between 0.0 and 5.0. |
| SetDefaultCooldownDuration | Set the default duration of the cooldown state to Seconds. Seconds is clamped between 1.0 and 60.0. |
| SetGlobalTransform | Sets the global transform of this object. |
| StartCooldown | Enter the cooldown state for Seconds seconds. If the device is already in the cooldown state, re-enable it after Seconds seconds. Seconds is clamped to a minimum of 1.0. |
| TeleportTo | Teleports the creative_object to the specified Position and Rotation. |
| TeleportTo | Teleports the creative_object to the specified location defined by Transform, also applies rotation and scale accordingly. |
| TeleportTo | Teleports the creative_device to the specified location defined by Transform, also applies rotation and scale accordingly. |
