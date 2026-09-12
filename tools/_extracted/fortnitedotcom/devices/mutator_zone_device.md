Used to specify a zone where custom gameplay effects can be applied (e.g. gravity, no build, no weapons).
|  |  |
| Verse using statement | using { /Fortnite.com/Devices } |

## Inheritance Hierarchy
This class is derived from the following hierarchy, starting with creative_object:
| Name | Description |
| creative_object | Base class for creative devices and props. |
| creative_device_base | Base class for creative_device. |
| effect_volume_device | Base class for types of volumes with special gameplay properties. |

## Members
This class has both data members and functions.

### Data
| Data Member Name | Type | Description |
| AgentBeginsEmotingEvent | listenable(payload) | Signaled when an agent in this zone begins emoting. This will not signal if the agent is on the Safe Team or if Affects Players is disabled. Sends the agent that started emoting. |
| AgentEndsEmotingEvent | listenable(payload) | Signaled when an agent in this zone ends emoting. This will not signal if the agent is on the Safe Team or if Affects Players is disabled. Sends the agent that stopped emoting. |
| AgentEntersEvent | listenable(payload) | Signaled when an agent enters this zone. Sends the agent entering this zone. |
| AgentExitsEvent | listenable(payload) | Signaled when an agent exits this zone. Sends the agent exiting this zone. |

### Functions
| Function Name | Description |
| Disable | Disables this device. |
| Enable | Enables this device. |
| GetAgentsInVolume | Returns an array of agents that are currently occupying the volume. |
| GetGlobalTransform | Gets the global transform of this object. |
| GetTransform | Returns the transform of the creative_object with units in cm. You must check creative_object.IsValid before calling this if there is a possibility the object has been disposed or destroyed by gameplay. Otherwise a runtime error will result. |
| IsInVolume | Is true when Agent is in the zone. |
| MoveTo | Moves the creative_object to the specified Position and Rotation over the specified time, in seconds. If an animation is currently playing on the creative_object it will be stopped and put into the AnimationNotSet state. |
| MoveTo | Moves the creative_object to the specified Transform over the specified time, in seconds. If an animation is currently playing on the creative_object it will be stopped and put into the AnimationNotSet state. |
| MoveTo | Moves the creative_device to the specified Transform over the specified time, in seconds. If an animation is currently playing on the creative_device it will be stopped and put into the AnimationNotSet state. |
| SetGlobalTransform | Sets the global transform of this object. |
| TeleportTo | Teleports the creative_object to the specified Position and Rotation. |
| TeleportTo | Teleports the creative_object to the specified location defined by Transform, also applies rotation and scale accordingly. |
| TeleportTo | Teleports the creative_device to the specified location defined by Transform, also applies rotation and scale accordingly. |
| UpdateSelectedClass | Updates Selected Class to Agent's class. |
| UpdateSelectedTeam | Updates Selected Team to Agent's team. |
