Provides team and inventory configurations that go beyond the choices the My Island settings provide. Can also be used to customize individual devices and create variations in team setup.
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
| AllowTemporaryTeamMemberInvitations | ??logic | This variable maps to the 'Dynamic Team Emotes' user option. Modifying this value does not affect the state of any existing Temporary Team member. If a player is currently on a Temporary Team, they will maintain access to the leave team emote regardless of this value. Available values: If this option is unset, use the global setting configured in Island Settings If this is set to TRUE, it allows members of this team to Emote and invite other players to their team. If this is set to FALSE, it prevents members of this team from using an Emote to invite other players to this team. |
| EnemyEliminatedEvent | listenable(payload) | Signaled when an enemy of Team is eliminated by a team member. Sends the agent team member who eliminated the enemy. |
| TeamMemberEliminatedEvent | listenable(payload) | Signaled when a member of Team is eliminated. Sends the agent that was eliminated. |
| TeamMemberSpawnedEvent | listenable(payload) | Signaled when a member of Team is spawned.Sends the agent that has spawned. |
| TeamOutOfRespawnsEvent | listenable(payload) | Signaled when Team runs out of respawns. |

### Functions
| Function Name | Description |
| EndRound | Ends the round and Team wins the round. |
| GetGlobalTransform | Gets the global transform of this object. |
| GetTeamMembers | Returns an array of agents that are currently of the team defined by this device. |
| GetTransform | Returns the transform of the creative_object with units in cm. You must check creative_object.IsValid before calling this if there is a possibility the object has been disposed or destroyed by gameplay. Otherwise a runtime error will result. |
| IsOnTeam | Is true if Agent is on Team. |
| MoveTo | Moves the creative_object to the specified Position and Rotation over the specified time, in seconds. If an animation is currently playing on the creative_object it will be stopped and put into the AnimationNotSet state. |
| MoveTo | Moves the creative_object to the specified Transform over the specified time, in seconds. If an animation is currently playing on the creative_object it will be stopped and put into the AnimationNotSet state. |
| MoveTo | Moves the creative_device to the specified Transform over the specified time, in seconds. If an animation is currently playing on the creative_device it will be stopped and put into the AnimationNotSet state. |
| RemoveTemporaryMemberFromTeam | Removes the agent from its Temporary Team. Decides based on whether the agent was on a Temporary Team. This will return them to the team they were on before they joined a Temporary Team |
| RemoveTemporaryMembersFromTeam | Returns all temporary team members for this Device's Team Setting Value back to their original Teams. If the device is configured to All, then this function will remove all Temporary Team members from any Temporary Team they are on, returning them to their original team. |
| RespawnAtPlayerSpawner | Spawn Player from the most appropriate player_spawner_device available (team match, highest priority, enemy proximity, etc). Uses the device's Should Respawn Alive Players setting to control behavior when called on an alive player. If no valid spawner is found, the player will respawn from skydive. |
| RespawnAtPlayerSpawner | Spawn Player from the most appropriate player_spawner_device, selected from the provided SpawnerGroup array. Uses the device's Should Respawn Alive Players setting to control behavior when called on an alive player. If no valid spawner is found, the player will respawn from skydive. |
| SetGlobalTransform | Sets the global transform of this object. |
| TeleportTo | Teleports the creative_object to the specified Position and Rotation. |
| TeleportTo | Teleports the creative_object to the specified location defined by Transform, also applies rotation and scale accordingly. |
| TeleportTo | Teleports the creative_device to the specified location defined by Transform, also applies rotation and scale accordingly. |
