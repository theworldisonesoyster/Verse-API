Module import path: /Fortnite.com/Devices/CreativeAnimation
- Fortnite.com
- Devices
- CreativeAnimation InterpolationTypes

## Classes and Structs
| Name | Description |
| cubic_bezier_parameters | A structure for defining Bezier interpolation parameters. See https://en.wikipedia.org/wiki/B%C3%A9zier_curve for more info on Bezier curves. |
| keyframe_delta | Instead of specifying the actual keyframe positions, we specify the keyframe deltas. This allows us to treat the initial position of the prop as keyframe 0 and avoid the question of how to get the prop to its initial location. For a animation_mode.Loop animation, the net rotation and translation must both be zero. Each delta is interpreted as a world-space transformation to be concatenated onto the previous transform(s). |
| animation_controller | Used to move and animate the position of creative_prop objects. See creative_prop.GetAnimationController for information on acquiring an instance of an animation_controller for a given creative_prop. See SetAnimation for details on authoring movement and animations. |

## Enumerations
| Name | Description |
| animation_mode | Animation play modes. |
| animation_controller_state | animation_controller states. |
| await_next_keyframe_result | Results for animation_controller.AwaitNextKeyframe function. |
