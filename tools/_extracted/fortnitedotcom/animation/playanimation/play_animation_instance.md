An animation instance created from play_animation_controller.Play that can be queried and manipulated.
|  |  |
| Verse using statement | using { /Fortnite.com/Animation/PlayAnimation } |

## Members
This class has both data members and functions.

### Data
| Data Member Name | Type | Description |
| CompletedEvent | listenable(payload) | Event triggered when the animation is completed. |
| InterruptedEvent | listenable(payload) | Event triggered when the animation is interrupted. |
| BlendedInEvent | listenable(payload) | Event triggered when the animation has finished to blend out. |
| BlendingOutEvent | listenable(payload) | Event triggered when the animation is beginning to blend out. |

### Functions
| Function Name | Description |
| GetState | Returns the state of the animation playback. |
| Stop | Stops the animation. |
| Await | Helper function that waits for the animation to complete or be interrupted. |
| IsPlaying | Helper function that succeeds if the state is Playing, BlendingIn, or BlendingOut. |
