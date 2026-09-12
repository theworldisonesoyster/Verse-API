Use to create a sprite that players can trade in a weapon for a random legendary weapon or a custom item list.
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
| GrantTimerCompletedEvent | listenable(payload) | Triggers when the grant timer has completed. Sends the triggering agent. |
| WeaponConsumedEvent | listenable(payload) | Triggers when a player gives the Earth Sprite a weapon. Sends the triggering agent. |

### Functions
| Function Name | Description |
| Disable | Disable the device. |
| DisableItemGranting | Disable the device's ability to grant items. Can still interact and consume weapons. |
| DisableTradingForPlayer | Prevents the agent from trading. |
| Enable | Enable the device, and resets all trade counts the Sprite is tracking. |
| EnableItemGranting | Enable the device's ability to grant items. |
| EnableTradingForPlayer | Allows a agent to trade, and will reset the agent's trade count for this Sprite. |
| GetGlobalTransform | Gets the global transform of this object. |
| GetTransform | Returns the transform of the creative_object with units in cm. You must check creative_object.IsValid before calling this if there is a possibility the object has been disposed or destroyed by gameplay. Otherwise a runtime error will result. |
| Hide | Makes the Earth Sprite invisible. |
| IsEnabled | Succeeds if the device is enabled, fails if it's disabled. |
| MoveTo | Moves the creative_object to the specified Position and Rotation over the specified time, in seconds. If an animation is currently playing on the creative_object it will be stopped and put into the AnimationNotSet state. |
| MoveTo | Moves the creative_object to the specified Transform over the specified time, in seconds. If an animation is currently playing on the creative_object it will be stopped and put into the AnimationNotSet state. |
| MoveTo | Moves the creative_device to the specified Transform over the specified time, in seconds. If an animation is currently playing on the creative_device it will be stopped and put into the AnimationNotSet state. |
| SetGlobalTransform | Sets the global transform of this object. |
| Show | Makes the Earth Sprite visible. |
| TeleportTo | Teleports the creative_object to the specified Position and Rotation. |
| TeleportTo | Teleports the creative_object to the specified location defined by Transform, also applies rotation and scale accordingly. |
| TeleportTo | Teleports the creative_device to the specified location defined by Transform, also applies rotation and scale accordingly. |
