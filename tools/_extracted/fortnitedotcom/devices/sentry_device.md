Generates an AI bot that spawns in a location and usually attacks players when they come in range.
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
| AlertedEvent | listenable(payload) | Signaled when the sentry is alerted to an agent. Sends the agent who alerted the sentry. |
| AttackingEvent | listenable(payload) | Signaled when a sentry attacks an agent. Sends the agent who is being attacked. |
| EliminatedEvent | listenable(payload) | Signaled when a sentry is eliminated. Sends the agent that eliminated the sentry. If the sentry was eliminated by a non-agent then false is returned. |
| EliminatingACreatureEvent | listenable(payload) | Signaled when the sentry eliminates a creature. |
| EliminatingAgentEvent | listenable(payload) | Signaled when a sentry eliminates an agent. Sends the agent who was eliminated by the sentry. |
| EntersAlertCooldownEvent | listenable(payload) | Signaled when the sentry enters the alert state. |
| ExitsAlertEvent | listenable(payload) | Signaled when the sentry exists the alert state. |

### Functions
| Function Name | Description |
| DestroySentry | Destroys the current sentry. |
| Disable | Disables this device. |
| Enable | Enables this device. |
| EnableAlert | Puts the sentry into the alert state. |
| GetGlobalTransform | Gets the global transform of this object. |
| GetTransform | Returns the transform of the creative_object with units in cm. You must check creative_object.IsValid before calling this if there is a possibility the object has been disposed or destroyed by gameplay. Otherwise a runtime error will result. |
| JoinTeam | Sets the sentry to the same team Agent is on. |
| MoveTo | Moves the creative_object to the specified Position and Rotation over the specified time, in seconds. If an animation is currently playing on the creative_object it will be stopped and put into the AnimationNotSet state. |
| MoveTo | Moves the creative_object to the specified Transform over the specified time, in seconds. If an animation is currently playing on the creative_object it will be stopped and put into the AnimationNotSet state. |
| MoveTo | Moves the creative_device to the specified Transform over the specified time, in seconds. If an animation is currently playing on the creative_device it will be stopped and put into the AnimationNotSet state. |
| Pacify | Puts the sentry into the pacify state, preventing from entering the alert (attacking) state. |
| ResetAlertCooldown | Resets the alert state. |
| ResetTeam | Resets the sentry to the original team designated in the device options. |
| SetGlobalTransform | Sets the global transform of this object. |
| Spawn | Spawns the sentry. |
| Target | Sets the sentry to target Agent. The sentry will not target agents on the same team as the sentry. |
| TeleportTo | Teleports the creative_object to the specified Position and Rotation. |
| TeleportTo | Teleports the creative_object to the specified location defined by Transform, also applies rotation and scale accordingly. |
| TeleportTo | Teleports the creative_device to the specified location defined by Transform, also applies rotation and scale accordingly. |
