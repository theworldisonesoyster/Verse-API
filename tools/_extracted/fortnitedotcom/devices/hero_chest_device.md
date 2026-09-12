An indestructible chest that can be locked and unlocked.
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
| ChestRank | ?hero_chest_rank | Determines the hologram that appears above the chest, as well as the loot the chest contains. From low to high, the ranks are C, B, A, and S. |
| LockedDescription | ?message | Descriptive text shown when interacting while the chest is locked. By default, this says 'You cannot open this right now.'. |
| LockedLabel | ?message | Main text shown when interacting while the chest is locked. The default is 'Rank X Chest' where X is the value of Rank. |
| LockedSublabel | ?message | Additional text shown when interacting while the chest is locked. By default, this says 'Unable to open'. |
| OpenEvent | listenable(payload) | Triggers whenever the chest is opened, returning the agent who opened it if applicable. |
| ShowHologram | ?logic | Whether to show the rank hologram while the chest is closed. |

### Functions
| Function Name | Description |
| Disable | Disable the device. While disabled, the chest can't be interacted with. |
| Enable | Enable the device, allowing interaction. |
| GetGlobalTransform | Gets the global transform of this object. |
| GetRankAsString | Returns the chest rank as a string. |
| GetTransform | Returns the transform of the creative_object with units in cm. You must check creative_object.IsValid before calling this if there is a possibility the object has been disposed or destroyed by gameplay. Otherwise a runtime error will result. |
| IsEnabled | Succeeds if the device is enabled, fails if it's disabled. |
| IsLocked | Succeeds if the chest is locked for Agent. |
| IsLockedForAll | Succeeds if the chest's default locked state is Locked. The default locked state is initialized by the Start Locked user option and is overridden by LockForAll and UnlockForAll. |
| IsOpen | Succeeds if the chest is currently open, fails if it's closed. |
| Lock | Lock the chest for Agent. Has no effect if the chest is open. |
| LockForAll | Lock the chest for everyone, and set this chest's default state to Locked. |
| MoveTo | Moves the creative_object to the specified Position and Rotation over the specified time, in seconds. If an animation is currently playing on the creative_object it will be stopped and put into the AnimationNotSet state. |
| MoveTo | Moves the creative_object to the specified Transform over the specified time, in seconds. If an animation is currently playing on the creative_object it will be stopped and put into the AnimationNotSet state. |
| MoveTo | Moves the creative_device to the specified Transform over the specified time, in seconds. If an animation is currently playing on the creative_device it will be stopped and put into the AnimationNotSet state. |
| Open | Open the chest. |
| Reset | Close the chest, refresh its loot, and set the chest to its default locked state for everyone. The default locked state is initialized by the Start Locked user option and is overridden by LockForAll and UnlockForAll. |
| SetGlobalTransform | Sets the global transform of this object. |
| TeleportTo | Teleports the creative_object to the specified Position and Rotation. |
| TeleportTo | Teleports the creative_object to the specified location defined by Transform, also applies rotation and scale accordingly. |
| TeleportTo | Teleports the creative_device to the specified location defined by Transform, also applies rotation and scale accordingly. |
| Unlock | Unlock the chest for Agent. Has no effect if the chest is open. |
| UnlockForAll | Unlock the chest for everyone, and set this chest's default state to Unlocked. |
