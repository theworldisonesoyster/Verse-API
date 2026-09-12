Allows creation and HUD tracking of custom objectives for agents to complete.
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
| CompleteEvent | listenable(payload) | Signaled when the tracked value reaches GetTarget for an agent. Sends the agent that reached GetTarget for their tracked value. |

### Functions
| Function Name | Description |
| Assign | Assigns the device to Agent (and any agents sharing progress). |
| AssignToAll | Assigns this device to all valid agents. |
| ClearPersistence | Clears tracked progress for Agent. Only valid if Use Persistence is set to Use. |
| Complete | The objective immediately completes. |
| DecreaseTargetValue | Decreases the target value for Agent by 1. |
| Decrement | Decrease the tracked value by Amount to Change on Received Signal for Agent. |
| GetActiveAgents | Returns an array of agents that currently have this tracker active. |
| GetGlobalTransform | Gets the global transform of this object. |
| GetTarget | Returns the target value that must be achieved in order for CompleteEvent to trigger. Clamped to 0 <= GetTarget <= 10000. |
| GetTransform | Returns the transform of the creative_object with units in cm. You must check creative_object.IsValid before calling this if there is a possibility the object has been disposed or destroyed by gameplay. Otherwise a runtime error will result. |
| GetValue | Returns the current total tracked value for all players. |
| GetValue | Returns the current total tracked value for the team at TeamIndex. |
| GetValue | Returns the current tracked value for Agent. |
| HasReachedTarget | Is true if Agent has reached the TargetValue for the tracker. |
| IncreaseTargetValue | Increases the target value for Agent by 1. |
| Increment | Increases the tracked value by Amount to Change on Received Signal for Agent. |
| IsActive | Is true if Agent currently has the tracker active. |
| Load | Loads tracked progress for Agent. Only valid if Use Persistence is set to Use. |
| LoadForAll | Loads tracked progress for all valid agents. Only valid if Use Persistence is set to Use. |
| MoveTo | Moves the creative_object to the specified Position and Rotation over the specified time, in seconds. If an animation is currently playing on the creative_object it will be stopped and put into the AnimationNotSet state. |
| MoveTo | Moves the creative_object to the specified Transform over the specified time, in seconds. If an animation is currently playing on the creative_object it will be stopped and put into the AnimationNotSet state. |
| MoveTo | Moves the creative_device to the specified Transform over the specified time, in seconds. If an animation is currently playing on the creative_device it will be stopped and put into the AnimationNotSet state. |
| Remove | Removes this device from Agent (and any agents sharing progress). |
| RemoveFromAll | Removes this device from all valid agents. |
| Reset | Resets the progress for Agent (and any agents sharing progress). |
| Save | Saves tracked progress for Agent. Only valid if Use Persistence is set to Use. |
| SetDescriptionText | Sets a description for the tracker_device, which is displayed if Show on HUD is enabled. Text has a 64 character limit. |
| SetGlobalTransform | Sets the global transform of this object. |
| SetTarget | Sets the target value that must be achieved in order for CompleteEvent to trigger. Clamped to 0 <= TargetValue <= 10000. |
| SetTitleText | Sets the title for the tracker_device, which is displayed if Show on HUD is enabled. Text has a 32 character limit. |
| SetValue | Sets the current tracked value for the device for all active players. |
| SetValue | Sets the current tracked value for the device for the Team at the TeamIndex. If Sharing is set to Individual, this will set the value for all team members. If Sharing is set to All, this will set the value for all players. |
| SetValue | Sets the current tracked value for the device for a specific 'Agent'. If Sharing is set to Team, this will set the value for their team. If Sharing is set to All, this will set the value for everyone. |
| TeleportTo | Teleports the creative_object to the specified Position and Rotation. |
| TeleportTo | Teleports the creative_object to the specified location defined by Transform, also applies rotation and scale accordingly. |
| TeleportTo | Teleports the creative_device to the specified location defined by Transform, also applies rotation and scale accordingly. |
