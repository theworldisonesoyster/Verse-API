Main API implemented by Fortnite characters.
|  |  |
| Verse using statement | using { /Fortnite.com/Characters } |

## Exposed Interfaces
This interface exposes the following interfaces:
| Name | Description |
| positional | Implemented by objects to allow reading position information. |
| healable | Implemented by Fortnite objects that can be healed. |
| healthful | Implemented by Fortnite objects that have health state and can be eliminated. |
| damageable | Implemented by Fortnite objects that can be damaged. |
| shieldable | Implemented by Fortnite objects that have shields. A shield is a method of protection that can take incoming damage while leaving the health state unchanged. |
| game_action_instigator | Implemented by Fortnite objects that initiate game actions, such as damage and heal. For example, player or agents. Event listeners often use game_action_instigators to calculate player damage scores. |
| game_action_causer | Implemented by Fortnite objects that can be passed through game action events, such as damage and heal. For example: player, vehicle, or weapon. Event Listeners often use game_action_causer to pass along additional information about what weapon caused the damage. Systems will then use that information for completing quests or processing game specific event logic. |

## Members
This interface has functions, but no data members.

### Functions
| Function Name | Description |
| GetAgent | Returns the agent associated with this fort_character. Use this when interacting with APIs that require an agent reference. |
| EliminatedEvent | Signaled when this fort_character is eliminated from the match. |
| GetViewRotation | Returns the rotation where this fort_character is looking or aiming at. |
| GetViewLocation | Returns the location where this fort_character is looking or aiming from. |
| JumpedEvent | Signaled when this fort_character jumps. Returns a listenable with a payload of this fort_character. |
| CrouchedEvent | Signaled when this fort_character changes crouch state. Sends tuple payload: 0: the fort_character that changed crouch states. 1: true if the character is crouching. false if the character is not crouching. |
| SprintedEvent | Signaled when this fort_character changes sprint state. Sends tuple payload: 0: the fort_character that changed sprint state. 1: true if the character is sprinting. false if the character stopped sprinting. |
| IsActive | Succeeds if this fort_character is in the world and has not been eliminated. Most fort_character actions will silently fail if this fails. Please test IsActive if you want to handle these failure cases rather than allow them to silently fail. |
| IsDownButNotOut | Succeeds if this fort_character is in the 'Down But Not Out' state. In this state the character is down but can still be revived by teammates for a period of time. |
| IsCrouching | Succeeds if this fort_character is crouching. |
| IsOnGround | Succeeds if this fort_character is standing on the ground. |
| IsInAir | Succeeds if this fort_character is standing in the air. |
| IsInWater | Succeeds if this fort_character is inside water volume. |
| IsFalling | Succeeds if this fort_character is in falling locomotion state. |
| IsGliding | Succeeds if this fort_character is in gliding locomotion state. |
| IsFlying | Succeeds if this fort_character is in flying locomotion state. |
| PutInStasis | Puts this fort_character into stasis, preventing certain types of movement specified by Args. |
| ReleaseFromStasis | Release this fort_character from stasis. |
| Show | Sets this fort_character visibility to visible. |
| Hide | Sets this fort_character visibility to invisible. |
| SetVulnerability | Control if this fort_character can be damaged. |
| IsVulnerable | Succeeds if this fort_character can be damaged. Fails if this fort_character cannot be damaged. |
| TeleportTo | Teleports this fort_character to the provided Position and applies the yaw and pitch of Rotation. Will fail if the Position specified is e.g. outside of the playspace or specifies a place where the character cannot fit. |
| GetEntity | Returns the entity associated with this fort_character. Use this when interacting with APIs that require an entity reference. |
| GetLinearVelocity | Returns a ‘fort_character’s linear velocity in meters/second. |
| SetLinearVelocity | Set a ‘fort_character’s linear velocity in meters/second. Will not do anything if physics is disabled. |
| ApplyLinearImpulse | Apply a linear impulse to a ‘fort_character’ with units in Newton*seconds. Will not do anything if physics is disabled. |
| GetMass | Returns a ‘fort_character’s mass in kilograms. |
| ApplyForce | Apply a force to a ‘fort_character’ with units in Newtons. Will not do anything if physics is disabled. |
