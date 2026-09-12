Used to track and react to how many players are in a particular area, and optionally display that information in game.
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
| CountedEvent | listenable(payload) | Signaled when a valid player enters the zone and is counted. The frequency of evaluation against the Target Player Count can be controlled through the device settings. Sends the agent that is now being counted. |
| CountFailsEvent | listenable(payload) | Signaled when the player count does not match Target Player Count. The frequency of evaluation against Target Player Count can be controlled through the device settings. |
| CountSucceedsEvent | listenable(payload) | Signaled when the player count matches Target Player Count. The frequency of evaluation against Target Player Count can be controlled through the device settings. |
| RemovedEvent | listenable(payload) | Signaled when a player is no longer counted by this device, such as when they leave the zone, leave the game, or are assigned to a different team or class. Sends the agent that is no longer being counted. |

### Functions
| Function Name | Description |
| CompareToTarget | Triggers an evaluation of the current count vs Target Player Count, signaling CountSucceedsEvent or CountFailsEvent based on the evaluation result. |
| DecrementTargetCount | Decrements Target Player Count by 1. Immediately triggers a new comparison. |
| Disable | Disables this device. |
| Enable | Enables this device. |
| GetCount | Returns the number of players currently counted by this device |
| GetCountedAgents | Returns an array of agents that are currently counted by the device. |
| GetGlobalTransform | Gets the global transform of this object. |
| GetTargetCount | Returns the number of players required for this counter to succeed. |
| GetTransform | Returns the transform of the creative_object with units in cm. You must check creative_object.IsValid before calling this if there is a possibility the object has been disposed or destroyed by gameplay. Otherwise a runtime error will result. |
| HideInfoPanel | Hide this device info panel from the world. |
| IncrementTargetCount | Increments Target Player Count by 1. Immediately triggers a new comparison. |
| IsCounted | Is true if Agent is currently counted by this device. |
| IsPassingTest | Is true if the device is currently succeeding in its comparison. |
| IsShowingInfoPanel | Returns whether this device is represented in the world as an info panel showing Current + Required player counts. |
| MoveTo | Moves the creative_object to the specified Position and Rotation over the specified time, in seconds. If an animation is currently playing on the creative_object it will be stopped and put into the AnimationNotSet state. |
| MoveTo | Moves the creative_object to the specified Transform over the specified time, in seconds. If an animation is currently playing on the creative_object it will be stopped and put into the AnimationNotSet state. |
| MoveTo | Moves the creative_device to the specified Transform over the specified time, in seconds. If an animation is currently playing on the creative_device it will be stopped and put into the AnimationNotSet state. |
| Register | Adds the player to the registered player list. Track Registered Players determines how registered players are counted. |
| Reset | Resets Target Player Count to the default value defined in the device settings. If Target Player Count was previously incremented or decremented, this reset immediately triggers a new comparison. |
| SetGlobalTransform | Sets the global transform of this object. |
| SetTargetCount | Sets the number of players required for this counter to succeed. Immediately triggers a new comparison. |
| ShowInfoPanel | Show this device in the world as an info panel showing Current + Required player counts. |
| TeleportTo | Teleports the creative_object to the specified Position and Rotation. |
| TeleportTo | Teleports the creative_object to the specified location defined by Transform, also applies rotation and scale accordingly. |
| TeleportTo | Teleports the creative_device to the specified location defined by Transform, also applies rotation and scale accordingly. |
| TransmitForAllCounted | Triggers CountedEvent for all agents currently being counted. |
| Unregister | Removes the player from the registered player list. Track Registered Players determines how registered players are counted. |
| UnregisterAll | Clears all players from the list of registered players. Track Registered Players determines how registered players are counted. |
