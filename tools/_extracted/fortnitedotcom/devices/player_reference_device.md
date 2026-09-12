Used to relay agent statistics to other devices and agents. Can transmit statistics such as elimination count, eliminated count, or scores when certain conditions are met. Can also project a hologram of the agent and display text that can be altered in various positions and curvatures.
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
| ActivatedEvent | listenable(payload) | Signaled when this device is activated. Sends the agent stored in the device. |
| AgentReplacedEvent | listenable(payload) | Signaled when the agent tracked by this device is replaced. Sends the new agent stored in the device. |
| AgentUpdatedEvent | listenable(payload) | Signaled when the agent tracked by this device is updated. Sends the new agent stored in the device. |
| AgentUpdateFailsEvent | listenable(payload) | Signaled when the agent tracked by this fails to be updated. Sends the agent that attempted to be stored in this device. |
| TrackedStatChangedEvent | listenable(payload) | Signaled when a stat tracked by this device is updated. Sends the agent stored in the device. |

### Functions
| Function Name | Description |
| Activate | Ends the round/game. |
| Clear | Clears the state of this device. |
| Disable | Disables this device. |
| Enable | Enables this device. |
| GetAgent | Returns the agent currently referenced by the device. |
| GetGlobalTransform | Gets the global transform of this object. |
| GetStatValue | Returns the stat value that this device is currently tracking |
| GetTransform | Returns the transform of the creative_object with units in cm. You must check creative_object.IsValid before calling this if there is a possibility the object has been disposed or destroyed by gameplay. Otherwise a runtime error will result. |
| IsReferenced | Is true when Agent is the player being referenced by the device. |
| MoveTo | Moves the creative_object to the specified Position and Rotation over the specified time, in seconds. If an animation is currently playing on the creative_object it will be stopped and put into the AnimationNotSet state. |
| MoveTo | Moves the creative_object to the specified Transform over the specified time, in seconds. If an animation is currently playing on the creative_object it will be stopped and put into the AnimationNotSet state. |
| MoveTo | Moves the creative_device to the specified Transform over the specified time, in seconds. If an animation is currently playing on the creative_device it will be stopped and put into the AnimationNotSet state. |
| Register | Registers Agent as the agent being tracked by this device. |
| SetGlobalTransform | Sets the global transform of this object. |
| TeleportTo | Teleports the creative_object to the specified Position and Rotation. |
| TeleportTo | Teleports the creative_object to the specified location defined by Transform, also applies rotation and scale accordingly. |
| TeleportTo | Teleports the creative_device to the specified location defined by Transform, also applies rotation and scale accordingly. |
