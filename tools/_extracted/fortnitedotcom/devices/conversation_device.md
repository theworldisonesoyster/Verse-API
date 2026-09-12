Used to set and trigger conversations made via the Conversation Graph. The conversation triggered is assigned to the device.
|  |  |
| Verse using statement | using { /Fortnite.com/Devices } |

## Inheritance Hierarchy
This class is derived from the following hierarchy, starting with creative_object:
| Name | Description |
| creative_object | Base class for creative devices and props. |
| creative_device_base | Base class for creative_device. |

## Exposed Interfaces
This class exposes the following interfaces:
| Name | Description |
| enableable | Implemented by classes whose instances can be enabled and disabled. |

## Members
This class has both data members and functions.

### Data
| Data Member Name | Type | Description |
| AllowedConversationCount | ?int | Sets the number of conversations allowed at once with the device. This will not make any conversations exit if there are more current conversations than allowed after this call. |
| CancelEvent | listenable(payload) | Signalled when a conversation has ended early by EndConversation or EndConversationForAll. |
| CharactersPerSecond | ??float | The constant rate that characters are revealed over the course of a second when a Speech node activates. The exact characters in the respective speech node are revealed and do not combine into glyphs. When the value is changed, active conversations are not updated. Works with the Box and Custom UI. The value of CharactersPerSecond is the default value used when initiating a conversation. CharactersPerSecond will be clamped between 0.25 and 100.0. If set to false all the characters will reveal instantly. |
| EndEvent | listenable(payload) | Signalled when a conversation has ended. |
| IndicatorBubbleRange | ?float | The range that the Indicator Bubble will be seen at. Clamps to range[0, 25]. |
| OnConversationEvent | listenable(payload) | Signaled when a choice node tied to this event is selected by an agent. Sends the agent that triggered the event, and EventNumber is the number specified in the Conversation Event node. |
| ShowConversationTextInWorldSpace | ?logic | Whether the device will show conversation text in worldspace when using the Radial UI type. |
| ShowIndicatorBubble | ?logic | whether the device will show the Indicator Bubble when nearby. |
| ShowNameWhenNearby | ?logic | Whether the device will show the Speaker when nearby. |
| SpeakerName | ?message | The Speaker Name of the device. When the value is changed, active conversations are not updated. The value of SpeakerName is the default value used when initiating a conversation. |

### Functions
| Function Name | Description |
| CanInitiateConversation | Check if an agent can initiate a conversation. |
| Disable | Disables this device. A disabled conversation device will not listen for inputs and trigger conversations. |
| Enable | Enables this device. An enabled conversation device will listen for inputs and trigger conversations. |
| EndConversation | Ends the assigned conversation with the agent. |
| EndConversationForAll | Ends all active conversations with this device. |
| GetActiveConversationsCount | Returns the count of currently-active conversations with this device. |
| GetGlobalTransform | Gets the global transform of this object. |
| GetTransform | Returns the transform of the creative_object with units in cm. You must check creative_object.IsValid before calling this if there is a possibility the object has been disposed or destroyed by gameplay. Otherwise a runtime error will result. |
| HideConversation | Hide the conversation UI for an 'agent'. Responses cannot be selected while the UI is hidden. This will work with Box and Custom UI. |
| InitiateConversation | Begins the assigned conversation with the agent. The conversation will not start if the device or the agent are otherwise incapable of having a conversation. |
| IsAgentInConversation | Check if an agent is in an active conversation. |
| IsEnabled | Check if the device is enabled. |
| MoveTo | Moves the creative_object to the specified Position and Rotation over the specified time, in seconds. If an animation is currently playing on the creative_object it will be stopped and put into the AnimationNotSet state. |
| MoveTo | Moves the creative_object to the specified Transform over the specified time, in seconds. If an animation is currently playing on the creative_object it will be stopped and put into the AnimationNotSet state. |
| MoveTo | Moves the creative_device to the specified Transform over the specified time, in seconds. If an animation is currently playing on the creative_device it will be stopped and put into the AnimationNotSet state. |
| SetGlobalTransform | Sets the global transform of this object. |
| ShowConversation | Show the conversation UI for an 'agent'. This will work with Box and Custom UI. |
| TeleportTo | Teleports the creative_object to the specified Position and Rotation. |
| TeleportTo | Teleports the creative_object to the specified location defined by Transform, also applies rotation and scale accordingly. |
| TeleportTo | Teleports the creative_device to the specified location defined by Transform, also applies rotation and scale accordingly. |
