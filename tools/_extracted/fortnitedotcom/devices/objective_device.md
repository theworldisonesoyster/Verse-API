Provides a collection of destructible devices that you can select from to use as objectives in your game.
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
| healable | Implemented by Fortnite objects that can be healed. |

## Members
This class has both data members and functions.

### Data
| Data Member Name | Type | Description |
| DestroyedEvent | listenable(payload) | Signaled when this device has been destroyed by an agent. Sends the agent that destroyed this device. |

### Functions
| Function Name | Description |
| ActivateObjectivePulse | Activates an objective pulse at Agent's location pointing toward this device. |
| Damage |  |
| Damage |  |
| DamagedEvent |  |
| DeactivateObjectivePulse | Deactivates the objective pulse at Agent's location. |
| Destroy | Destroys the objective item. This is done regardless of the visibility or health of the item. |
| GetGlobalTransform | Gets the global transform of this object. |
| GetHealth |  |
| GetMaxHealth |  |
| GetTransform | Returns the transform of the creative_object with units in cm. You must check creative_object.IsValid before calling this if there is a possibility the object has been disposed or destroyed by gameplay. Otherwise a runtime error will result. |
| Heal |  |
| Heal |  |
| HealedEvent |  |
| Hide | Hides this device from the world. |
| MoveTo | Moves the creative_object to the specified Position and Rotation over the specified time, in seconds. If an animation is currently playing on the creative_object it will be stopped and put into the AnimationNotSet state. |
| MoveTo | Moves the creative_object to the specified Transform over the specified time, in seconds. If an animation is currently playing on the creative_object it will be stopped and put into the AnimationNotSet state. |
| MoveTo | Moves the creative_device to the specified Transform over the specified time, in seconds. If an animation is currently playing on the creative_device it will be stopped and put into the AnimationNotSet state. |
| SetGlobalTransform | Sets the global transform of this object. |
| SetHealth |  |
| SetInvulnerable | Sets the device either invulnerable or damageable |
| SetMaxHealth |  |
| Show | Shows this device in the world. |
| TeleportTo | Teleports the creative_object to the specified Position and Rotation. |
| TeleportTo | Teleports the creative_object to the specified location defined by Transform, also applies rotation and scale accordingly. |
| TeleportTo | Teleports the creative_device to the specified location defined by Transform, also applies rotation and scale accordingly. |
