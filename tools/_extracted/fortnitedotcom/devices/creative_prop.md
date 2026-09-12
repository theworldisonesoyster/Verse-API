A Fortnite prop that has been placed or spawned in the island.
|  |  |
| Verse using statement | using { /Fortnite.com/Devices } |

## Inheritance Hierarchy
This class is derived from creative_object.
| Name | Description |
| creative_object | Base class for creative devices and props. |

## Exposed Interfaces
This class exposes the following interfaces:
| Name | Description |
| invalidatable | Implemented by classes whose instances can become invalid at runtime. |

## Members
This class has both data members and functions.

### Data
| Data Member Name | Type | Description |
| CanBeDamaged | ?logic | Enable/disable whether this prop can be damaged. If disabled, the creative prop will not take damage from attacks. |

### Functions
| Function Name | Description |
| ApplyAngularImpulse | Apply an angular impulse to a ‘creative_prop’ with units in Newtonmeterseconds. Will not do anything if physics is disabled. |
| ApplyForce | Apply a force to a ‘creative_prop’ with units in Newtons. Will not do anything if physics is disabled. |
| ApplyLinearImpulse | Apply a linear impulse to a ‘creative_prop’ with units in Newton*seconds. Will not do anything if physics is disabled. |
| ApplyTorque | Apply a torque to a ‘creative_prop’ with units in Newton*meters. Will not do anything if physics is disabled. |
| Dispose | Destroys the creative_prop and remove it from the island. |
| GetAngularVelocity | Returns a ‘creative_prop’s angular velocity in radians/second. |
| GetDynamic | Get whether a ‘creative_prop’ is dynamic (affected by physics functions). |
| GetGlobalTransform | Gets the global transform of this object. |
| GetLinearVelocity | Returns a ‘creative_prop’s linear velocity in meters/second. |
| GetMass | Returns a ‘creative_prop’s mass in kilograms. |
| GetTransform | Returns the transform of the creative_object with units in cm. You must check creative_object.IsValid before calling this if there is a possibility the object has been disposed or destroyed by gameplay. Otherwise a runtime error will result. |
| Hide | Hides the creative_prop in the world and disable collisions. |
| IsDisposed | Succeeds if this object has been disposed of either via Dispose() or through an external system. |
| IsValid | Succeeds if this object has not been disposed of either via Dispose() or through an external system. |
| MoveTo | Moves the creative_object to the specified Position and Rotation over the specified time, in seconds. If an animation is currently playing on the creative_object it will be stopped and put into the AnimationNotSet state. |
| MoveTo | Moves the creative_object to the specified Transform over the specified time, in seconds. If an animation is currently playing on the creative_object it will be stopped and put into the AnimationNotSet state. |
| MoveTo | Moves the creative_device to the specified Transform over the specified time, in seconds. If an animation is currently playing on the creative_device it will be stopped and put into the AnimationNotSet state. |
| SetAngularVelocity | Set a ‘creative_prop’s angular velocity in radians/seconds. Will not do anything if physics is disabled. |
| SetDynamic | Set whether a ‘creative_prop’ is dynamic (affected by physics functions). Will not do anything if physics is disabled OR the prop does not have a FortPhysicsComponent. |
| SetGlobalTransform | Sets the global transform of this object. |
| SetLinearVelocity | Set a ‘creative_prop’s linear velocity in meters/second. Will not do anything if physics is disabled. |
| SetMaterial | Changes the Material of the Mesh used by this instance. Optionally can specify which Mesh element index to apply the material to, otherwise defaults to the 0 (default) Mesh element |
| SetMesh | Changes the Mesh used by this instance. |
| Show | Shows the creative_prop in the world and enable collisions. |
| TeleportTo | Teleports the creative_object to the specified Position and Rotation. |
| TeleportTo | Teleports the creative_object to the specified location defined by Transform, also applies rotation and scale accordingly. |
| TeleportTo | Teleports the creative_device to the specified location defined by Transform, also applies rotation and scale accordingly. |
