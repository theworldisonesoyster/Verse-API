Main API implemented by Fortnite vehicles.
|  |  |
| Verse using statement | using { /Fortnite.com/Vehicles } |

## Exposed Interfaces
This interface exposes the following interfaces:
| Name | Description |
| positional | Implemented by objects to allow reading position information. |
| healthful | Implemented by Fortnite objects that have health state and can be eliminated. |
| damageable | Implemented by Fortnite objects that can be damaged. |
| game_action_causer | Implemented by Fortnite objects that can be passed through game action events, such as damage and heal. For example: player, vehicle, or weapon. Event Listeners often use game_action_causer to pass along additional information about what weapon caused the damage. Systems will then use that information for completing quests or processing game specific event logic. |
| showable | Implemented by classes whose instances can change visibility to be shown or hidden. |

## Members
This interface has both data members and functions.

### Data
| Data Member Name | Type | Description |
| Speed | ?float | The current speed of the vehicle in m/s. |
| BoostRemaining | ??float | The boost state of the vehicle. If the vehicle uses boost, this value will be between 0.0 and BoostCapacity. Otherwise, this value will be false. |
| BoostCapacity | ??float | The maximum boost capacity of the vehicle. If the vehicle uses boost, this value will be between 1.0 and Inf. Otherwise, this value will be false. |

### Functions
| Function Name | Description |
| IsOnGround | Succeeds if this fort_vehicle is standing on ground. |
| IsInAir | Succeeds if this fort_vehicle is standing in air. |
| IsInWater | Succeeds if this fort_vehicle is standing in water. |
| GetPassengers |  |
| GetOccupants | Returns an array with all agent currently occupying the vehicle. |
| GetDrivers | Returns an array with all the current drivers of the vehicle, which is usually a single agent. |
| GetFuelRemaining | Returns the fuel state of the vehicle. If the vehicle uses fuel, this value will be between 0.0 and GetFuelCapacity. Otherwise, this value will be -1.0. |
| GetFuelCapacity | Returns the maximum fuel capacity of the vehicle. If the vehicle uses fuel, this value will be between 1.0 and Inf. Otherwise, this value will be -1.0. |
| TeleportTo | Teleports the fort_vehicle to the specified Position and Rotation. |
| RemoveAgent | Removes the specified agent from the vehicle. Fails if the agent is not in the vehicle. |
| RemoveAll | Removes all occupying agents from the vehicle. |
| AddAgent | Attempts to add the agent to the fort_vehicle. If there are no empty seats, or the agent cannot otherwise be placed in the vehicle, the operation fails. |
| GetSeats | Returns an array of all fort_vehicle_seats in the fort_vehicle. |
