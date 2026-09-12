Interface used to trigger easing behaviors
|  |  |
| Verse using statement | using { /Verse.org/SceneGraph } |

## Exposed Interfaces
This interface exposes the following interfaces:
| Name | Description |
| cancelable | Implemented by classes that allow users to cancel an operation. For example, calling subscribable.Subscribe with a callback returns a cancelable object. Calling Cancel on the return object unsubscribes the callback. |

## Members
This interface has functions, but no data members.

### Functions
| Function Name | Description |
| EaseOut | Trigger an ease-out. Triggering an ease-out again when already easing-out, or when fully eased-out has no effect |
| EaseOut | Trigger an ease-out. If an easing_window is provided here, then it will override any previously provided window. Triggering an ease-out again when already easing-out, or when fully eased-out has no effect |
