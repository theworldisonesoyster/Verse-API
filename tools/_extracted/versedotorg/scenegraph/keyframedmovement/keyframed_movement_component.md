Provides teleportation and simple keyframe-based animation for an entity. Animations play back in the Pre-Physics tick phase. When animating an entity with a parent_constraint, animation will be relative to the parent entity.
|  |  |
| Verse using statement | using { /Verse.org/SceneGraph/KeyframedMovement } |

## Inheritance Hierarchy
This class is derived from component.
| Name | Description |
| component | Base class for authoring logic and data in the SceneGraph. Using components you can author re-usable building blocks of logic and data which can then be added to entities in the scene. Components are a very low level building block which can be used in many ways. For example: Exposing engine level concepts like mesh or sound Adding gameplay capabilities like damage or interaction Storing an inventory for a character in the game As components are generic there is no specific way that they must be used. It is up to the needs of your experience if you use one big game component or if you break up logic into many small components. Classes deriving from component must also specify <final_super> to be added to entities. This ensures the class will always derive directly from component. Further subclassing of the initial derived component is allowed and does not require specifying <final_super> on the derived classes. Only one instance of a component from each subclass group can be added to an entity at a time. For example, given this group of components, only one light_component can exist on a single entity. To create multiple lights you should use multiple entities. light_component := class(component){} capsule_light_component := class(light_component){} directional_light_component := class(light_component){} spot_light_component := class(light_component){} sphere_light_component := class(light_component){} rect_light_component := class(light_component){} ============================================================================== Component Lifetime Components move through a series of lifetime functions as they are added to entities, added to the scene, and begin running in the simulation. Components should override these methods to perform setup and run their simulation. As a component shuts down it will then move through shutdown version of these functions, giving users the opportunity to clean up any retained state on the component before it is disposed . Lifetime M |

## Members
This class has both data members and functions.

### Data
| Data Member Name | Type | Description |
| Duration | ??float | Gets the duration in seconds this keyframed movement will take. Fails if a fixed duration is not known (ex: looping animations). |
| Entity | entity | The parent entity of this component. Components must have a parent entity pointer provided when being constructed. Components cannot be moved between parents. |
| FinishedEvent | unknown | Get the event that fires when the animations ends, failing if the animation is of infinite duration |
| KeyframeReachedEvent | unknown | Signaled when any keyframe is reached. (Keyframe:int, IsReversed:logic). |
| PausedEvent | unknown | Get the event that fires when the animation is Paused. |
| PlayedEvent | unknown | Get the event that fires when the animation begins or resumes Playing. |
| StoppedEvent | unknown | Get the event that fires when the animation is Stopped. |
| TickEvents | ?tick_events | Set callbacks to TickEvents.PrePhysics and TickEvents.PostPhysics to receive per-frame updates before and after physics is updated on your object. |

### Functions
| Function Name | Description |
| HasValidAnimation | Is there a valid set of playable keyframes? |
| IsInScene | Succeeds if the component is currently in the scene. After OnAddedToScene is called this call succeeds. After OnRemovingFromScene is called this call fails. |
| IsPaused | Is the animation paused? |
| IsPlaying | Is the animation currently playing? |
| IsSimulating | Succeeds if the component is currently simulating. After OnBeginSimulation is called this call succeeds. After OnEndSimulation is called this call fails. |
| OnAddedToScene | Called when the component is added to the scene by parenting it under the simulation entity or another entity already in the scene. Querying for components in the scene is valid after this phase completes. |
| OnBeginSimulation | Called when the component begins simulating within the scene. Use this to set up TickEvent callbacks or other setup that must be guaranteed to complete immediately. OnAddedToScene is guaranteed to run before OnBeginSimulation. |
| OnEndSimulation | Called when the component ends simulation within the scene. Simulation ends on a component when the experience resets, the parent entity is removed from the scene. Cached TickEvents cancelables should be canceled in OnEndSimulation. OnSimulate task will be canceled before OnEndSimulation is called. OnEndSimulation is only called on components that have already had OnBeginSimulation called. |
| OnReceive | Respond to a scene event. Return true to consume the event and halt propagation to the next entity. |
| OnRemovingFromScene | Called when the component is about to be removed from the scene. Components are removed from a scene when the parent entity is removed from the scene. OnRemovingFromScene is only called on components that have already had OnAddedToScene called. |
| OnSimulate | Called when the component begins simulating within the scene. Use this to add asynchronous/suspends update logic for a component. OnBeginSimulation is guaranteed to run before OnSimulate. OnSimulate will be cancelled before OnEndSimulation |
| Pause | Pause movement. Subsequently calling Play() will resume from the point in the animation when it was paused. |
| Play | Begin or resume playback. |
| RemoveFromEntity | Removes the component from the entity. Removed components are removed from the scene and can only be added back to the same entity. Flows through OnEndSimulation-> OnRemovingFromScene. |
| SendDown | Send a scene event to this component, invoking OnReceive. Returns true if any participant consumed the event. |
| SetKeyframes | Stop any ongoing animation, sets the animation path and rebases it relative to the actor's current transform. Does not start playing until you call Play(). |
| Stop | Stop and reset transform to the initial state. Subsequently calling Play() will begin the animation anew. |
| Stop | Stop and reset transform to the initial state. Subsequently calling Play() will begin the animation anew. |
