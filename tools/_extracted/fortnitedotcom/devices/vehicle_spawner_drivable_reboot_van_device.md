|  |  |
| Verse using statement | using { /Fortnite.com/Devices } |

## Inheritance Hierarchy
This class is derived from the following hierarchy, starting with creative_object:
| Name | Description |
| creative_object | Base class for creative devices and props. |
| creative_device_base | Base class for creative_device. |
| vehicle_spawner_device | Base class for various specialized vehicle spawners which allow specific vehicle types to be spawned and configured with specialized options. |

## Exposed Interfaces
This class exposes the following interfaces:
| Name | Description |
| reboot_van_interface |  |

## Members
This class has both data members and functions.

### Data
| Data Member Name | Type | Description |
| AgentEntersVehicleEvent | listenable(payload) | Signaled when an agent enters the vehicle. Sends the agent that entered the vehicle. |
| AgentExitsVehicleEvent | listenable(payload) | Signaled when an agent exits the vehicle. Sends the agent that exited the vehicle. |
| CanPurchaseRebootCard | ?logic | Determines if players can purchase an eliminated player's reboot card. |
| DecayRateMultiplier | ??float | Multiplier on the decay rate of reboot progress. Clamped between 0.1 and 2.0. Only used if RebootProgressDecay is set to Custom Decay. |
| DestroyedEvent | listenable(payload) | Signaled when a vehicle is destroyed. |
| PurchaseRebootCardOptions | ??reboot_card_purchase_options | Purchase reboot card options. Only used if CanPurchaseRebootCard is true. |
| RebootCardPurchaseEvent | listenable(payload) | Triggers when a player purchases a Reboot Card. agent is the player that purchased the Reboot Card. |
| RebootEvent | listenable(payload) | Triggers when Reboot Van has finished rebooting a set of players. agentis the player that started the reboot. |
| RebootProgressDecay | ?reboot_progress_decay_behavior | How quickly reboot progress decays when nobody is interacting with the Reboot Van. Custom Decay - Set a custom multiplier on the decay rate. Instant Reset - Instantly reset progress to zero. Battle Royale - Use Battle Royale's decay rate. |
| RechargeCompleteEvent | listenable(payload) | Triggers when Reboot Van has finished recharging. agent is the last interacting player. |
| RechargeTimer | ?float | The remaining time (in seconds) on the recharge timer. Clamped between 0.0 and 3600.0. If there is no active timer, getting returns 0.0. If there is no active timer, setting does nothing. |
| RechargeTimerLength | ?float | The length of the recharge timer in seconds, regardless of the timer's current state. Clamped between 0.0 and 3600.0. |
| ReviveCompleteEvent | listenable(payload) | Triggers when Reboot Van has finished reviving a player from DBNO. agent is the player that was just revived. |
| SpawnedEvent | listenable(payload) | Signaled when a vehicle is spawned or respawned by this device. Sends the fort_vehicle who was spawned. |
| Vehicle | ??fort_vehicle | The fort_vehicle currently associated with this spawner, if one exists. |
| VehicleDestroyedEvent | listenable(payload) | Signaled when a vehicle is destroyed. Deprecated, use DestroyedEvent instead. |
| VehicleSpawnedEvent | listenable(payload) | Signaled when a vehicle is spawned or respawned by this device. Deprecated, use SpawnedEvent instead. |

### Functions
| Function Name | Description |
| AssignDriver | Sets agent as the vehicle's driver. |
| DestroyVehicle | Destroys the vehicle if it exists. |
| Disable | Disables this device. |
| DisableReboot | Disable the device. |
| DisableRevive | Disable the revival seat. |
| Enable | Enables this device. |
| EnableReboot | Enable the device. |
| EnableRevive | Enable the revival seat. |
| GetGlobalTransform | Gets the global transform of this object. |
| GetTransform | Returns the transform of the creative_object with units in cm. You must check creative_object.IsValid before calling this if there is a possibility the object has been disposed or destroyed by gameplay. Otherwise a runtime error will result. |
| IsEnabledReboot | Succeeds if the device is enabled, fails if it's disabled. |
| IsEnabledRevive | Succeeds if the revival seat is enabled, fails if it's disabled. |
| MoveTo | Moves the creative_object to the specified Position and Rotation over the specified time, in seconds. If an animation is currently playing on the creative_object it will be stopped and put into the AnimationNotSet state. |
| MoveTo | Moves the creative_object to the specified Transform over the specified time, in seconds. If an animation is currently playing on the creative_object it will be stopped and put into the AnimationNotSet state. |
| MoveTo | Moves the creative_device to the specified Transform over the specified time, in seconds. If an animation is currently playing on the creative_device it will be stopped and put into the AnimationNotSet state. |
| RespawnVehicle | Spawns a new vehicle. The previous vehicle will be destroyed before a new vehicle spawns. |
| SetGlobalTransform | Sets the global transform of this object. |
| TeleportTo | Teleports the creative_object to the specified Position and Rotation. |
| TeleportTo | Teleports the creative_object to the specified location defined by Transform, also applies rotation and scale accordingly. |
| TeleportTo | Teleports the creative_device to the specified location defined by Transform, also applies rotation and scale accordingly. |
