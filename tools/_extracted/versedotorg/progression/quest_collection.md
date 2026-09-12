The source of truth for quest participation.
|  |  |
| Verse using statement | using { /Verse.org/Progression } |

## Members
This class has both data members and functions.

### Data
| Data Member Name | Type | Description |
| JoinEvent | unknown | Signaled when a participant joins any quest in this collection. |
| AbandonEvent | unknown | Signaled when a participant abandons any quest in this collection. |
| CompleteEvent | unknown | Signaled when any quest in this collection completes. |
| Quests | ?[quest][]quest_membership | All memberships indexed by quest. |
| Participants | ?[quest_participant][]quest_membership | All memberships indexed by participant. |

### Functions
| Function Name | Description |
| JoinQuest | Adds 'Participant' to 'Quest' with the given participation info. |
| AbandonQuest | Removes 'Participant' from 'Quest'. |
