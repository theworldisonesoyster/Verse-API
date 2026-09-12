Used to spawn customizable boxes containing vehicle mods. Hit a box with a vehicle to apply the mod.
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
| enableable | Implemented by classes whose instances can be enabled and disabled. |

## Members
This class has both data members and functions.

### Data
| Data Member Name | Type | Description |
| BoxDestroyedEvent | listenable(payload) | Triggers whenever the mod box is destroyed regardless of whether a mod was applied. Returns tuple: 0: The agent that triggered this event, if applicable. 1: The index int of the chosen mod in the device's list, starting with 0 for Custom List Mod 1. If Possible Mods is not set to Custom List, int will be -1. |
| BoxSpawnedEvent | listenable(payload) | Triggers whenever the mod box spawns. Returns the index int of the chosen mod in the device's list, starting with 0 for Custom List Mod 1. If Possible Mods is not set to Custom List, int will be -1. |
| ModAppliedEvent | listenable(payload) | Triggers whenever the mod is applied to a vehicle. Returns tuple: 0: The agent driving the vehicle, if applicable. 1: The fort_vehicle the mod applied to. 2: The index int of the chosen mod in the device's list, starting with 0 for Custom List Mod 1. If Possible Mods is not set to Custom List, int will be -1. |
| ModApplyFailedEvent | listenable(payload) | Triggers whenever the mod fails to apply to a vehicle. Returns tuple: 0: The agent driving the vehicle, if applicable. 1: The fort_vehicle the mod failed to apply to. 2: The index int of the chosen mod in the device's list, starting with 0 for Custom List Mod 1. If Possible Mods is not set to Custom List, int will be -1. |
| ModApplyOverriddenEvent | listenable(payload) | If ModAppliedEvent is overridden (see SetOverrideModApplyEvent), breaking a mod box triggers this instead of ModAppliedEvent, ModApplyFailEvent, or NoModEvent. Returns tuple: 0: The agent driving the vehicle, if applicable. 1: The fort_vehicle the mod would attempt to apply to. 2: The index int of the chosen mod in the device's list, starting with 0 for Custom List Mod 1. If Possible Mods is not set to Custom List, int will be -1. |
| ModBoxCustomListSettings | ?[]vehicle_mod_box_settings | An array containing the custom settings for each entry in the device's custom list. Index 0 applies to Custom List Mod 1, index 1 applies to Custom List Mod 2, and so on. The contents of each entry in the array can be individually set and returned. If Possible Mods is not set to Custom List, this array will be empty. |
| ModBoxOverallSettings | ?vehicle_mod_box_settings | Contains the custom settings for Overall Visual Style, which can be individually set and returned. |
| NoModEvent | listenable(payload) | Triggers whenever a No Mod entry from a custom list tries to apply to a vehicle. Returns tuple: 0: The agent driving the vehicle, if applicable. 1: The fort_vehicle that broke the box. 2: The index int of the specific No Mod entry in the device's list, starting with 0 for Custom List Mod 1. |

### Functions
| Function Name | Description |
| CycleToNextValidIndex | If the mod box is spawned, respawn it as the next valid entry in the list without triggering BoxDestroyEvent. If the mod box is not spawned, that will be the next mod box. The list wraps, which means the first index is considered directly after the last index. Does nothing if this device is disabled or Possible Mods is not set to Custom List. |
| CycleToPreviousValidIndex | If the mod box is spawned, respawn it as the previous valid entry in the list without triggering BoxDestroyEvent. If the mod box is not spawned, that will be the next mod box. The list wraps, which means the last index is considered directly before the first index. Does nothing if this device is disabled or Possible Mods is not set to Custom List. |
| DespawnBox | Despawn the box and clear the spawn timer without triggering BoxDestroyEvent. The respawn hologram will be visible, but will not progress without StartSpawnTimer. The device must be enabled. |
| Disable | Disable the device and clear any active spawn timer. While disabled, it will be hidden and vehicle mod boxes will not spawn. |
| Enable | Enable the device and start the spawn timer. While enabled, it can spawn vehicle mod boxes, and those boxes can be interacted with. |
| GetActiveTimerRemaining | Returns the remaining time (in seconds) of the device's active spawn timer. If there is no active timer, return 0.0. |
| GetCurrentIndex | Returns the current index int in the device's list of mod boxes. This value is set whenever the device spawns a new mod box. The device's list starts with 0 for Custom List Mod 1. If Possible Mods is not set to Custom List or the device has never spawned a mod box, int will be -1. |
| GetGlobalTransform | Gets the global transform of this object. |
| GetInitialSpawnTimerLength | Returns the total length of the initial spawn timer in seconds, regardless of the timer's current state. |
| GetRespawnTimerLength | Returns the total length of the respawn timer in seconds, regardless of the timer's current state. |
| GetSpawnCount | Returns the number of times the device has spawned a mod box. |
| GetTransform | Returns the transform of the creative_object with units in cm. You must check creative_object.IsValid before calling this if there is a possibility the object has been disposed or destroyed by gameplay. Otherwise a runtime error will result. |
| IsEnabled | Succeeds if the object is enabled, fails if it's disabled. |
| IsSpawned | Check if this device currently has a spawned mod box. |
| IsValidIndex | Succeeds if Index is a valid entry in the device's list. Fails if Index is an invalid entry or Possible Mods is not set to Custom List. |
| MoveTo | Moves the creative_object to the specified Position and Rotation over the specified time, in seconds. If an animation is currently playing on the creative_object it will be stopped and put into the AnimationNotSet state. |
| MoveTo | Moves the creative_object to the specified Transform over the specified time, in seconds. If an animation is currently playing on the creative_object it will be stopped and put into the AnimationNotSet state. |
| MoveTo | Moves the creative_device to the specified Transform over the specified time, in seconds. If an animation is currently playing on the creative_device it will be stopped and put into the AnimationNotSet state. |
| ResetModBoxName | Reset the names of this device's mod boxes, if the name has been customized. |
| ResetPlayerTooltip | Reset the text of the tooltip that appears when a player gets close to the mod box without a vehicle, if it's been customized. |
| SetCustomModBoxName | Set this device's mod boxes to use the name Name The displayed name will not exceed 50 characters. The following characters are disallowed: {, }, <, >, \, /, and |. |
| SetCustomPlayerTooltipText | Set the Text of the tooltip that appears when a player gets close to the mod box without a vehicle. The displayed text will not exceed 50 characters. The following characters are disallowed: {, }, <, >, \, /, and |. |
| SetGlobalTransform | Sets the global transform of this object. |
| SetInitialSpawnTimer | Set the remaining time (in seconds) on the initial spawn timer (clamped to a minimum of 0.0). The device must be enabled. Even if the initial spawn timer is not currently active, this sets its length. |
| SetNextModIndex | Set the next mod box to spawn to be the one at Index in the device's list. The first index in the list is 0 for Custom List Mod 1. Does nothing if this device is disabled, Possible Mods is not set to Custom List, or Index is invalid. |
| SetOverrideModApplyEvent | If Override is true, destroying the mod box with a vehicle will trigger ModApplyOverriddenEvent and a mod will not be applied. In this case, destroying the mod box will not trigger ModAppliedEvent, ModApplyFailEvent, or NoModEvent. The values returned by ModApplyOverriddenEvent can be used for TryApplyModByAgent and TryApplyModByVehicle, so the event can be handled manually. See ModApplyOverriddenEvent for more information. |
| SetRespawnTimer | Set the remaining time (in seconds) on the respawn timer (clamped to a minimum of 0.0). The device must be enabled. This also sets the length of this device's future respawn timers. |
| SpawnBox | Spawn a mod box if the device is enabled. If one is already spawned, spawn a new one without triggering BoxDestroyEvent. |
| SpawnLastChosenMod | Spawn the same mod box this device spawned before the current one. If a mod box is already spawned, despawn that first without triggering BoxDestroyEvent. Does nothing if this device is disabled or has not spawned more than one mod box. |
| SpawnModBoxByIndex | Spawn the mod box at Index in the device's list. If a mod box is already spawned, despawn that first without triggering BoxDestroyEvent. The first index in the list is 0 for Custom List Mod 1. Does nothing if this device is disabled, Possible Mods is not set to Custom List, or Index is invalid. |
| StartSpawnTimer | Despawn the box if necessary without triggering BoxDestroyEvent, then start the spawn timer. The device must be enabled. |
| TeleportTo | Teleports the creative_object to the specified Position and Rotation. |
| TeleportTo | Teleports the creative_object to the specified location defined by Transform, also applies rotation and scale accordingly. |
| TeleportTo | Teleports the creative_device to the specified location defined by Transform, also applies rotation and scale accordingly. |
| TryApplyModByAgent | Apply the mod at Index in the device's list to the vehicle that Agent is riding. The first index in the list is 0 for Custom List Mod 1. Triggers ModAppliedEvent, ModApplyFailEvent, and NoModEvent as appropriate, regardless of SetOverrideModApplyEvent. Fails if this device is disabled, Possible Mods is not set to Custom List, Index or Agent is invalid, or Agent is not riding a vehicle. |
| TryApplyModByVehicle | Apply the mod at Index in the device's list to Vehicle. The first index in the list is 0 for Custom List Mod 1. Triggers ModAppliedEvent, ModApplyFailEvent, and NoModEvent as appropriate, regardless of SetOverrideModApplyEvent. Fails if this device is disabled, Possible Mods is not set to Custom List, or Index or Vehicle is invalid. Vehicle must be an actual fort_vehicle. A vehicle spawner device will not be valid. ModApplyOverriddenEvent, ModAppliedEvent, ModApplyFailEvent, and NoModEvent are a few ways to get a fort_vehicle value. |
