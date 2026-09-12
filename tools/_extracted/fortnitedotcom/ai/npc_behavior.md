Inherit from this to create a custom NPC behavior. The npc_behavior can be defined for a character in a CharacterDefinition asset, or in a npc_spawner_device.
|  |  |
| Verse using statement | using { /Fortnite.com/AI } |

## Members
This class has functions, but no data members.

### Functions
| Function Name | Description |
| OnBegin | This function is called when the NPC is added to the simulation. |
| OnEnd | This function is called when the NPC is removed from the simulation. |
| GetAgent | Returns the agent associated with this behavior. |
| GetEntity | Returns the entity associated with this behavior. |
