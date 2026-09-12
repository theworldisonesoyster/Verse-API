Used to increase or decrease a stat for an agent.
|  |  |
| Verse using statement | using { /Fortnite.com/Devices } |

## Inheritance Hierarchy
This class is derived from the following hierarchy, starting with creative_object:
| Name | Description |
| creative_object | Base class for creative devices and props. |
| creative_device_base | Base class for creative_device. |
| powerup_device | Base class for various powerup devices offering common events like ItemPickedUpEvent. |

## Members
This class has both data members and functions.

### Data
| Data Member Name | Type | Description |
| ItemPickedUpEvent | listenable(payload) | Signaled when the powerup is picked up by an agent. Sends the agent that picked up the powerup. |

### Functions
| Function Name | Description |
| Clear | Removes the powerup effect from Agent. |
| ClearForAll | Removes the powerup effect without an agent reference. Requires Apply To set to All Players. |
| Despawn | Despawns this powerup from the experience. |
| GetDuration | Returns the Duration that this powerup will be active for on any player it is applied to. |
| GetGlobalTransform | Gets the global transform of this object. |
| GetMagnitude | Returns the current Magnitude for the powerup. For the Stat Powerup, this is the value of the stat that the powerup will add or remove to a player that picks up the powerup. |
| GetRemainingTime | If the Agent has the effect applied to them, this will return the remaining time the effect has. Returns -1.0 if the effect has an infinite duration. Returns 0.0 if the Agent does not have the effect applied. |
| GetTransform | Returns the transform of the creative_object with units in cm. You must check creative_object.IsValid before calling this if there is a possibility the object has been disposed or destroyed by gameplay. Otherwise a runtime error will result. |
| HasEffect | Returns the Agent has the powerup's effect (or another of the same type) applied to them. |
| IsSpawned | Succeeds if the powerup is currently spawned. |
| MoveTo | Moves the creative_object to the specified Position and Rotation over the specified time, in seconds. If an animation is currently playing on the creative_object it will be stopped and put into the AnimationNotSet state. |
| MoveTo | Moves the creative_object to the specified Transform over the specified time, in seconds. If an animation is currently playing on the creative_object it will be stopped and put into the AnimationNotSet state. |
| MoveTo | Moves the creative_device to the specified Transform over the specified time, in seconds. If an animation is currently playing on the creative_device it will be stopped and put into the AnimationNotSet state. |
| Pickup | Grants this powerup to Agent. |
| Pickup | Grants this powerup without an agent reference. Requires Apply To set to All Players. |
| SetDuration | Updates the Duration for this powerup, clamped to the Min and Max defined in the device. Will not apply to any currently applied effects. |
| SetGlobalTransform | Sets the global transform of this object. |
| SetMagnitude | Sets the Magnitude for this powerup, clamped to the Min and Max defined in the device. Will not apply to any currently applied effects. For the Stat Powerup, this is the value of the stat that the powerup will add or remove to a player that picks up the powerup. |
| Spawn | Spawns the powerup into the experience so users can interact with it. |
| TeleportTo | Teleports the creative_object to the specified Position and Rotation. |
| TeleportTo | Teleports the creative_object to the specified location defined by Transform, also applies rotation and scale accordingly. |
| TeleportTo | Teleports the creative_device to the specified location defined by Transform, also applies rotation and scale accordingly. |
