Used to spawn guards that can patrol and attack other agents. Changing properties will only affect newly spawned guards.
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
| Accuracy | ?guard_spawner_accuracy | Determines how the guard uses its VisibilityRange as defined by guard_spawner_visibility_range_restriction. |
| AlertedEvent | listenable(payload) | Signaled when a guard has identified an opponent. Source is the guard who is aware. Target is the agent who alerted the guard. |
| CanBeHired | ?logic | If true, agents can hire the guard. |
| DamagedEvent | listenable(payload) | Signaled when guard is damaged. Source is the agent that damaged the guard. If the guard was damaged by a non-agent then false is returned. Target is the guard that was damaged. |
| DespawnOnDismissal | ?logic | Determines if the guard despawns when it is dismissed. |
| DismissedEvent | listenable(payload) | Signaled when a guard is dismissed by a player. Source is the agent who dismissed the guard. Target is the guard that was dismissed. |
| DisplayAlertness | ?logic | Determines if the guard displays its alertness level over its head. |
| EliminatedEvent | listenable(payload) | Signaled when a guard is eliminated. Source is the agent that eliminated the guard. If the guard was eliminated by a non-agent then Source is 'false'. Target is the guard that was eliminated. |
| EliminatingEvent | listenable(payload) | Signaled when a guard eliminates an agent. Source is the guard that eliminated the agent. Target is the agent that was eliminated. |
| HiredEvent | listenable(payload) | Signaled when a guard is hired by a player. Source is the agent who hired the guard. Target is the guard that was hired. |
| InitialHealth | ?float | Determines the starting health of the guard. This value is clamped between 1 and 10000. |
| InitialShield | ?float | Determines the starting shield of the guard. This value is clamped between 1 and 10000. |
| Invincible | ?logic | Whether the guard can receive damage. |
| MaxHealth | ?float | The health value of the guard. This value is clamped between 1 and 10000. |
| MaxShield | ?float | Determines the maximum shield value of the guard. This value is clamped between 1 and 10000. |
| ObeyCommands | ?logic | Determines if the guard obeys ping commands from its hired player. |
| PatrolRange | ?float | Distance in centimeters from its spawn position from which the guard will peacefully roam. This value is clamped between 200.0 and 25000.0. |
| RestoreHealthAndShieldOnHire | ?logic | Determines if the guard is healed when it is hired. |
| ShowHealthBar | ?logic | If true, displays the guard's health to players. |
| SpawnedEvent | listenable(payload) | Signaled when a guard is spawned. Sends the agent guard who was spawned. |
| SuspiciousEvent | listenable(payload) | Signaled when a guard becomes suspicious. Sends the agent guard who is suspicious. |
| TargetLostEvent | listenable(payload) | Signaled when a guard has lost track of a target. Source is the guard that lost track of a target. Target is the agent no longer targeted by the guard. |
| UnawareEvent | listenable(payload) | Signaled when a guard becomes unaware. Sends the agent guard who is unaware. |
| VisibilityRange | ?float | Determines the range, in centimeters, from which the guard will respond. This value is clamped between 0.0 and 25000.0. |
| VisibilityRangeRestriction | ?guard_spawner_visibility_range_restriction | Determines how the guard uses its VisibilityRange as defined by guard_spawner_visibility_range_restriction. |

### Functions
| Function Name | Description |
| Despawn | Despawns guards. |
| Despawn | Despawns guards. Instigator will be considered as the eliminator of those guards. |
| Disable | Disables this device. Guards will despawn if Despawn Guards When Disabled is set. |
| DismissAgentHiredGuards | Dismisses all hired guards that were recruited by Instigator. |
| DismissAllHiredGuards | Dismisses all hired guards. |
| Enable | Enables this device. Guards will start to spawn. |
| ForceAttackTarget | Forces guards to attack Target, bypassing perception checks. 'ForgetTime' ranges from 0.0 to 600.0 (in seconds, default is 600.0), it is the time after which the target will be ignored if not found. 'ForgetDistance' ranges from 0.0 to 100000.0 (in centimeters, default is 100000.0), it is the distance at which the target will be ignored if not found. |
| GetAgents | Get all agents created by this device. |
| GetGlobalTransform | Gets the global transform of this object. |
| GetName | Gets the name of the guard in the hire the guard conversation and elimination feed. |
| GetSpawnLimit | Returns the spawn limit of the device. |
| GetTransform | Returns the transform of the creative_object with units in cm. You must check creative_object.IsValid before calling this if there is a possibility the object has been disposed or destroyed by gameplay. Otherwise a runtime error will result. |
| Hire | Hires guards to Instigator's team. |
| MoveTo | Moves the creative_object to the specified Position and Rotation over the specified time, in seconds. If an animation is currently playing on the creative_object it will be stopped and put into the AnimationNotSet state. |
| MoveTo | Moves the creative_object to the specified Transform over the specified time, in seconds. If an animation is currently playing on the creative_object it will be stopped and put into the AnimationNotSet state. |
| MoveTo | Moves the creative_device to the specified Transform over the specified time, in seconds. If an animation is currently playing on the creative_device it will be stopped and put into the AnimationNotSet state. |
| Reset | Resets the spawn count allowing spawning of a new batch of guards. |
| SetGlobalTransform | Sets the global transform of this object. |
| SetGuardsHireable | Allows guards to be hired. |
| SetGuardsNotHireable | Prevents guards from being hired. |
| SetName | Sets the name of the guard in the hire the guard conversation and elimination feed. |
| Spawn | Tries to spawn a guard. |
| Spawn | Tries to spawn a guard. If Auto Hire When Spawned is set to Triggering Player the guard will be hired by Instigator. |
| SpawnAt | Spawn a guard at the given position. When Rotation is not provided, it will default to the Devices rotation. Returns the agent spawned or false if the device has reached its maximum spawn count. This function is ` because it takes time to load the NPC before it can be returned. |
| TeleportTo | Teleports the creative_object to the specified Position and Rotation. |
| TeleportTo | Teleports the creative_object to the specified location defined by Transform, also applies rotation and scale accordingly. |
| TeleportTo | Teleports the creative_device to the specified location defined by Transform, also applies rotation and scale accordingly. |
