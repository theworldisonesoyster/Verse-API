Specialized trigger_base_device that will fire output events based on line of sight between agents and the device.
|  |  |
| Verse using statement | using { /Fortnite.com/Devices } |

## Inheritance Hierarchy
This class is derived from the following hierarchy, starting with creative_object:
| Name | Description |
| creative_object | Base class for creative devices and props. |
| creative_device_base | Base class for creative_device. |
| trigger_base_device | Base class for various specialized trigger devices. See also: trigger_device perception_trigger_device * attribute_evaluator_device |

## Members
This class has both data members and functions.

### Data
| Data Member Name | Type | Description |
| AgentLooksAtDeviceEvent | listenable(payload) | Signaled when an agent has direct line of sight to this device. Sends the agent that has seen this device. |
| AgentLooksAwayFromDeviceEvent | listenable(payload) | Signaled when an agent has lost direct line of sight to this device. Sends the agent that has lost sight of this device. |
| DeviceLosesSightOfAgentEvent | listenable(payload) | Signaled when this device loses direct line of sight to an agent. Sends the agent this device has lost sight of. |
| DeviceSeesAgentEvent | listenable(payload) | Signaled when this device has direct line of sight to an agent. Sends the agent seen by this device. |

### Functions
| Function Name | Description |
| Disable | Disables this device. |
| Enable | Enables this device. |
| GetGlobalTransform | Gets the global transform of this object. |
| GetLookingAtDeviceAgents | Returns an array of agents that are currently of the class defined by this device. |
| GetMaxTriggerCount | Gets the maximum amount of times this device can trigger. 0 indicates no limit on trigger count. |
| GetPerceivedAgents | Returns an array of agents that are currently of the class defined by this device. |
| GetResetDelay | Gets the time (in seconds) before the device can be triggered again (if MaxTrigger count allows). |
| GetTransform | Returns the transform of the creative_object with units in cm. You must check creative_object.IsValid before calling this if there is a possibility the object has been disposed or destroyed by gameplay. Otherwise a runtime error will result. |
| GetTransmitDelay | Gets the time (in seconds) which must pass after triggering, before this device informs other external devices that it has been triggered. |
| GetTriggerCountRemaining | Returns the number of times that this device can still be triggered before hitting GetMaxTriggerCount. Returns 0 if GetMaxTriggerCount is unlimited. |
| IsLookingAtDevice | Succeeds when Agent is registered to this checkpoint. |
| IsPerceived | Succeeds when Agent is registered to this checkpoint. |
| MoveTo | Moves the creative_object to the specified Position and Rotation over the specified time, in seconds. If an animation is currently playing on the creative_object it will be stopped and put into the AnimationNotSet state. |
| MoveTo | Moves the creative_object to the specified Transform over the specified time, in seconds. If an animation is currently playing on the creative_object it will be stopped and put into the AnimationNotSet state. |
| MoveTo | Moves the creative_device to the specified Transform over the specified time, in seconds. If an animation is currently playing on the creative_device it will be stopped and put into the AnimationNotSet state. |
| Reset | Resets the number of times this device has been activated. This will set GetTriggerCountRemaining back to 0 |
| SetGlobalTransform | Sets the global transform of this object. |
| SetMaxTriggerCount | Sets the maximum amount of times this device can trigger. 0 can be used to indicate no limit on trigger count. MaxCount is clamped between [0,20]. |
| SetResetDelay | Sets the time (in seconds) after triggering, before the device can be triggered again (if MaxTrigger count allows). |
| SetTransmitDelay | Sets the time (in seconds) which must pass after triggering, before this device informs other external devices that it has been triggered. |
| TeleportTo | Teleports the creative_object to the specified Position and Rotation. |
| TeleportTo | Teleports the creative_object to the specified location defined by Transform, also applies rotation and scale accordingly. |
| TeleportTo | Teleports the creative_device to the specified location defined by Transform, also applies rotation and scale accordingly. |
