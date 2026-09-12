Verse path: /Verse.org Module import path: /Verse.org/SpatialMath
- Verse.org
- SpatialMath

## Classes and Structs
| Name | Description |
| rotation | An abstract representation of an orientation change in 3d-space. |
| transform | A combination of scale, rotation, and translation, applied in that order. |
| vector3 | 3-dimensional vector with float components. |

## Functions
| Name | Description |
| MakeRotationRadians | Makes a rotation from Axis and Angle in radians using a right-handed sign convention (e.g. a positive rotation around Up takes Forward to Left). |
| MakeRotationDegrees | Degrees version of MakeRotationRadians |
| MakeRotationFromYawPitchRollRadians | Makes a rotation by applying a pre-rotation of YawAngle followed by PitchAngle and then RollAngle, in that order: yaw is right-handed rotation about the Down axis, pitch is right-handed rotation about the Right axis, roll is right-handed rotation about the Forward axis. |
| MakeRotationFromYawPitchRollDegrees | Degrees version of MakeRotationFromYawPitchRollRadians |
| MakeRotationFromEulerRadians | Makes a rotation by applying a post-rotation of LeftAxisAngle followed by UpAxisAngle and then ForwardAxisAngle in that order. Right-handed convention (e.g. a positive rotation around Up takes +Forward to Left). |
| MakeRotationFromEulerDegrees | Degrees version of MakeRotationFromEulerRadians |
| IdentityRotation | Makes the identity rotation. |
| Distance | Returns the distance between Rotation1 and Rotation2. The result will be between: 0.0, representing equivalent rotations and 1.0 representing rotations which are 180 degrees apart (i.e., the shortest rotation between them is 180 degrees around some axis). |
| AngularDistanceRadians | Returns the smallest angular distance between Rotation1 and Rotation2 in radians. |
| AngularDistanceDegrees | Degrees version of AngularDistanceRadians. |
| operator'*' | Apply a PreRotation to PostRotation as v * PreRotation * PostRotation. |
| MakeShortestRotationBetween | Makes the smallest angular rotation from InitialVector to FinalVector two vectors of arbitrary length such that: InitialVector * MakeShortestRotationBetween(InitialVector, FinalVector) = FinalVector and MakeShortestRotationBetween(InitialVector, FinalVector)?.GetAngleRadians() is as small as possible. |
| Slerp | Used to perform spherical linear interpolation between From (when Ratio = 0.0) and To (when Ratio = 1.0). Expects 0.0 <= Ratio <= 1.0. |
| operator'*' | Makes a vector3 by applying Rotation to Vector. |
| ToString | Makes a string representation of rotation in axis/degrees format with a right-handed sign convention. ToString(MakeRotationRadians(vector3{Left:=0.0, Up:=0.0, Forward:=1.0}, PiFloat/2.0)) produces the string: "{Axis = {Left=0.000000, Up=0.000000, Forward=1.000000}, Angle = 90.000000}". |
| DegreesToRadians | Returns radians from Degrees. |
| RadiansToDegrees | Returns degrees from Radians. |
| operator'*' | Makes a vector3 by applying InTransform to InVector. |
| ToString | Makes a string representation of InTransform where the result is on the form. "{Translation = {ToString(InTransform.Translation)}, Rotation = {ToString(InTransform.Rotation)}, Scale = {ToString(InTransform.Scale`)}}". |
| ReflectVector | Makes a vector3 by inverting the SurfaceNormal component of Direction. |
| DotProduct | Returns the dot product of V1 and V2. |
| CrossProductLeftHanded | Returns the left-handed cross product of V1 and V2. |
| CrossProduct | Returns the right-handed cross product of V1 and V2. |
| Distance | Returns the Euclidean distance between V1 and V2. |
| DistanceSquared | Returns the squared Euclidean distance between V1 and V2. |
| DistanceForwardLeft | Returns the 2-D Euclidean distance between V1 and V2 by ignoring the difference in Up. |
| DistanceSquaredForwardLeft | Returns the squared 2-D Euclidean distance between V1 and V2 by ignoring their difference in Up. |
| ToString | Makes a string representation of V. |
| Lerp | Used to linearly interpolate/extrapolate between From (when Parameter = 0.0) and To (when Parameter = 1.0). Expects that all arguments are finite. Returns From*(1 - Parameter) + To*Parameter. |
| prefix'-' | Makes a vector3 by inverting the signs of Operand. |
| operator'+' | Makes a vector3 by component-wise addition of Left and Right. |
| operator'-' | Makes a vector3 by component-wise subtraction of Right from Left. |
| operator'*' | Makes a vector3 by component-wise multiplication of Left and Right. |
| operator'*' | Makes a vector3 by multiplying the components of Left by Right. |
| operator'*' | Makes a vector3 by multiplying the components of Right by Left. |
| operator'/' | Makes a vector3 by dividing the components of Left by Right. |
| operator'/' | Makes a vector3 by component-wise division of Left by Right. |
| IsAlmostEqual | Succeeds when each component of V1 and V2 are within AbsoluteTolerance of each other. |
