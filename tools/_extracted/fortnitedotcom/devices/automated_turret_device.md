Used to create a customizable turret that can search for nearby targets.
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
| healable | Implemented by Fortnite objects that can be healed. |

## Members
This class has both data members and functions.

### Data
| Data Member Name | Type | Description |
| ActivatedEvent | listenable(payload) | Triggers when someone enters the activation radius while nobody else is there. Sends the activating agent. If the activator is a non-agent then false is returned. |
| DamagedEvent | listenable(payload) | Triggers when the turret is damaged. Sends the triggering agent. If the activator is a non-agent then false is returned. |
| DestroyedEvent | listenable(payload) | Triggers when the turret is destroyed. Sends the triggering agent. If the activator is a non-agent then false is returned. |
| TargetFoundEvent | listenable(payload) | Triggers when the turret finds a target. Sends the agent that was found. |
| TargetLostEvent | listenable(payload) | Triggers when the turret loses a target. Sends the agent that was lost. |

### Functions
| Function Name | Description |
| ClearTarget | Clears the turret's current target and returns the turret to searching for targets. If the current target is still in range, it'll likely be the best target, and will be reacquired. Combine with disabled targeting for best results. |
| Disable | Disables the turret, causing it to close and ignore its activation radius. |
| Enable | Enables the turret to rotate, target, and track. |
| GetGlobalTransform | Gets the global transform of this object. |
| GetHealth |  |
| GetMaxHealth |  |
| GetTarget | Returns the agent currently targeted by the device. |
| GetTransform | Returns the transform of the creative_object with units in cm. You must check creative_object.IsValid before calling this if there is a possibility the object has been disposed or destroyed by gameplay. Otherwise a runtime error will result. |
| Heal |  |
| Heal |  |
| HealedEvent |  |
| MoveTo | Moves the creative_object to the specified Position and Rotation over the specified time, in seconds. If an animation is currently playing on the creative_object it will be stopped and put into the AnimationNotSet state. |
| MoveTo | Moves the creative_object to the specified Transform over the specified time, in seconds. If an animation is currently playing on the creative_object it will be stopped and put into the AnimationNotSet state. |
| MoveTo | Moves the creative_device to the specified Transform over the specified time, in seconds. If an animation is currently playing on the creative_device it will be stopped and put into the AnimationNotSet state. |
| SetActivationRange | Sets the range in meters at which the turret will activate to Range. This is clamped between 2.0 and 100.0 meters. |
| SetDamage | Sets the amount of damage the turret will do per shot to targets to Damage. |
| SetGlobalTransform | Sets the global transform of this object. |
| SetHealth |  |
| SetMaxHealth |  |
| SetTarget | Set the supplied Agent as the turret's target. The target will only change if Agent is within the activation radius, has direct line-of-sight to the turret, is on a targetable team as determined by Possible Targets, and is not Down But Not Out. |
| SetTargetRange | Sets the range in meters at which the turret will target to Range. This is clamped between 2.0 and 100.0 meters. Setting it lower than 2m will disable Targeting. |
| SetTeam | Set the turret to the same team as the supplied Agent. Only usable if Possible Targets is not set to Everyone. |
| TeleportTo | Teleports the creative_object to the specified Position and Rotation. |
| TeleportTo | Teleports the creative_object to the specified location defined by Transform, also applies rotation and scale accordingly. |
| TeleportTo | Teleports the creative_device to the specified location defined by Transform, also applies rotation and scale accordingly. |
| UseDefaultTeam | Set the turret to the Default Team. Only usable if Possible Targets is not set to Everyone. |
| UseTeamWildlifeAndCreatures | Set the turret to the Wildlife & Creatures team. Only usable if Possible Targets is not set to Everyone. |
