Represents a seat in a fort_vehicle.
|  |  |
| Verse using statement | using { /Fortnite.com/Vehicles } |

## Members
This class has both data members and functions.

### Data
| Data Member Name | Type | Description |
| Occupant | ??agent | The agent currently occupying this seat, if any. |
| Vehicle | ?fort_vehicle | The fort_vehicle this seat belongs to. |

### Functions
| Function Name | Description |
| IsDriverSeat | Succeeds if this is a driver seat. |
| SetOccupant | Attempts to seat Agent into this seat. Fails if the seat is occupied or the agent cannot be seated. Setting the occupant to false will remove any seated agent. |
