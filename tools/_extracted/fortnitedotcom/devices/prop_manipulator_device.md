Used to manipulate the properties of one or more props in a specified area (e.g. Visibility/Destructibility).
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
| DamagedEvent | listenable(payload) | Signaled when props affected by this device are damaged. Sends the agent that damaged the prop. |
| DestroyedEvent | listenable(payload) | Signaled when props affected by this device are destroyed. Sends the agent that destroyed the prop. |
| HarvestingEvent | listenable(payload) | Signaled when prop resource nodes affected by this device are harvested. Sends the agent that harvested resources from the prop. |
| ResourceDepletionEvent | listenable(payload) | Signaled when prop resource nodes affected by this device are completely depleted of energy. Sends the agent that depleted the prop's energy. |

### Functions
| Function Name | Description |
| Disable | Disables this device. |
| DisableResourceNodeOverrides | Sets the Override Resource option to No. |
| Enable | Enables this device. |
| ExhaustResources | Empties the resources of all props affected by this device. |
| GetGlobalTransform | Gets the global transform of this object. |
| GetTransform | Returns the transform of the creative_object with units in cm. You must check creative_object.IsValid before calling this if there is a possibility the object has been disposed or destroyed by gameplay. Otherwise a runtime error will result. |
| HideProps | Hides all props affected by this device. |
| MoveTo | Moves the creative_object to the specified Position and Rotation over the specified time, in seconds. If an animation is currently playing on the creative_object it will be stopped and put into the AnimationNotSet state. |
| MoveTo | Moves the creative_object to the specified Transform over the specified time, in seconds. If an animation is currently playing on the creative_object it will be stopped and put into the AnimationNotSet state. |
| MoveTo | Moves the creative_device to the specified Transform over the specified time, in seconds. If an animation is currently playing on the creative_device it will be stopped and put into the AnimationNotSet state. |
| RestockResources | Restocks the resources of all props affected by this device. |
| RestoreHealth | Restores health of all props affected by this device. |
| SetGlobalTransform | Sets the global transform of this object. |
| SetResourceOverridesActive | Sets the Override Resource option to Yes. |
| ShowProps | Shows all props affected by this device. |
| TeleportTo | Teleports the creative_object to the specified Position and Rotation. |
| TeleportTo | Teleports the creative_object to the specified location defined by Transform, also applies rotation and scale accordingly. |
| TeleportTo | Teleports the creative_device to the specified location defined by Transform, also applies rotation and scale accordingly. |
