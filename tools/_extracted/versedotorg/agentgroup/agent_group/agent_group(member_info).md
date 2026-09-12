An agent group is defined as a set of agents that share a common ownership.This class stores agents and specific information about each member via the member_info type provided.
|  |  |
| Verse using statement | using { /Verse.org/AgentGroup } |

## Exposed Interfaces
This class exposes the following interfaces:
| Name | Description |
| agent_group_interface(member_info) | Interface that defines a class as providing an agent group. |

## Members
This class has both data members and functions.

### Data
| Data Member Name | Type | Description |
| AddMemberEvent | listenable(payload) | Signalled whenever an agent successfully joins this agent group.Passes in the agent that joined along with their member_info. |
| RemoveMemberEvent | listenable(payload) | Signalled whenever an agent successfully leaves this agent group.Passes in the agent that left along with their member_info. |
| MemberInfoChangeEvent | listenable(payload) | Signalled whenever the MemberInfo class is re-instantiated for a given agent.Passes in the agent that was updated along with their new member_info. |

### Functions
| Function Name | Description |
| GetMemberMap | Get the members of this agent group with their member info |
| AddMember | Attempt to add the given agent to this agent group.This function returns a result that will either succeed or return an error. |
| RemoveMember | Attempt to remove the given agent from this agent group.This function returns a result that will either succeed or return an error. |
