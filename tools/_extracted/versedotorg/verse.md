- Verse.org
- Verse Easing

## Classes and Structs
| Name | Description |
| classifiable_subset(element_type) | A classifiable_subset is a container that holds a set of elements. A classifiable_subset can hold multiple elements of the same type. |
| diagnostic | An opaque diagnostic message that only shows up in diagnostic logs. The format of the diagnostic may change at any time without warning and may not be inspected by Verse code. |
| event(t) | A recurring, successively signaled parametric event with a payload allowing a simple mechanism to coordinate between concurrent tasks. |
| locale | Used for message localization. |
| message | A localizable text message. |
| modifier_stack(t) | Modifier stacks provide an ordered application of modifiers. |

## Interfaces
| Name | Description |
| cancelable | Implemented by classes that allow users to cancel an operation. For example, calling subscribable.Subscribe with a callback returns a cancelable object. Calling Cancel on the return object unsubscribes the callback. |
| disposable | Implemented by classes whose instances have limited lifetimes. |
| enableable | Implemented by classes whose instances can be enabled and disabled. |
| invalidatable | Implemented by classes whose instances can become invalid at runtime. |
| showable | Implemented by classes whose instances can change visibility to be shown or hidden. |

## Functions
| Name | Description |
| operator'=' |  |
| operator'<>' |  |
| prefix'-' |  |
| operator'+' |  |
| operator'-' |  |
| operator'*' |  |
| operator'/' |  |
| operator'+=' |  |
| operator'-=' |  |
| operator'*=' |  |
| Abs |  |
| BitAnd |  |
| BitOr |  |
| BitXor |  |
| BitNot |  |
| operator'>' |  |
| operator'>=' |  |
| operator'<' |  |
| operator'<=' |  |
| Ceil |  |
| Floor |  |
| prefix'-' |  |
| operator'+' |  |
| operator'-' |  |
| operator'*' |  |
| operator'/' |  |
| operator'+=' |  |
| operator'-=' |  |
| operator'*=' |  |
| operator'/=' |  |
| Abs |  |
| operator'*' |  |
| operator'*' |  |
| operator'>' |  |
| operator'>=' |  |
| operator'<' |  |
| operator'<=' |  |
| operator'?' |  |
| operator'+' |  |
| operator'+=' |  |
| operator'()' |  |
| operator'()' |  |
| operator'()' |  |
| ConcatenateMaps |  |
| operator'()' |  |
| operator'()' |  |
| weak_map |  |
| operator'?' |  |
| FitsInPlayerMap |  |
| Print | Writes Message to a dedicated Print log while displaying it in Color on the client screen for Duration seconds. By default, Color is NamedColors.White and Duration is 2.0 seconds. |
| Print | Writes Message to a dedicated Print log while displaying it in Color on the client screen for Duration seconds. By default, Color is NamedColors.White and Duration is 2.0 seconds. |
| Print | Writes Message to a dedicated Print log while displaying it in Color on the client screen for Duration seconds. By default, Color is NamedColors.White and Duration is 2.0 seconds. |
| Concatenate | Makes a flattened array by concatenating the elements of Arrays. |
| classifiable_subset | A classifiable_subset is a container that holds a set of elements. A classifiable_subset can hold multiple elements of the same type. |
| MakeClassifiableSubset | Constructs a classifiable_subset containing the InElements. |
| operator'+' | Returns a new set that is the union of all elements in InSetL set and InSetR. |
| operator'+' | Concatenates two diagnostic messages. |
| operator'+' | Concatenates a diagnostic message with a normal string, yielding a diagnostic message. |
| operator'+' | Concatenates a normal string with a diagnostic message, yielding a diagnostic message. |
| ToDiagnostic | Converts any Verse value into an opaque diagnostic message. |
| Err | Halts the Verse runtime with error Message. |
| event | A recurring, successively signaled parametric event with a payload allowing a simple mechanism to coordinate between concurrent tasks. |
| event | A recurring, successively signaled event allowing a simple mechanism to coordinate between concurrent tasks. |
| Ceil | Returns the smallest int that is greater than or equal to Val. Fails if not IsFinite(Val). |
| Floor | Returns the largest int that is less than or equal to Val. Fails if not IsFinite(Val). |
| Round | Returns Val rounded to the nearest int. When the fractional part of Val is 0.5, rounds to the nearest even int (per the IEEE-754 default rounding mode). Fails if not IsFinite(Val). |
| Int | Returns the int that equals Val without the fractional part. Fails if not IsFinite(val). |
| ToString | Makes a string representation of Val. |
| GetSecondsSinceEpoch | Returns the number of seconds since January 1, 1970 UTC, ignoring leap seconds. I.e, this function implements Unix time. This function always returns the same value within the same transaction. |
| ToString | Makes a printable string representation of Val. |
| listenable | A parametric interface combining awaitable and subscribable. |
| listenable | A parameterless interface combining awaitable and subscribable. |
| Localize | Makes a string by localizing Message based on the current locale. |
| Join | Makes a message by concatenating Separator between the elements of Messages. |
| Clamp | Constrains the value of Val between A and B. Robustly handles different argument orderings. Returns the median of Val, A, and B, such that comparisons with NaN operate as if NaN > +Inf. |
| Clamp | Constrains the value of Val between A and B. Robustly handles different argument orderings. Returns the median of Val, A, and B. |
| Min | Returns the minimum of X and Y. |
| Max | Returns the maximum of X and Y. |
| Min | Returns the minimum of X and Y unless either are NaN. Returns NaN if either X or Y are NaN. |
| Max | Returns the maximum of X and Y unless either are NaN. Returns NaN if either X or Y are NaN. |
| Sqrt | Returns the square root of X if X >= 0.0. Returns NaN if X < 0.0. |
| Sin | Returns the sine of X, where X is interpreted as a value in radians, if IsFinite[X]. Returns NaN if not IsFinite[X]. |
| Cos | Returns the cosine of X, where X is interpreted as a value in radians, if IsFinite[X]. Returns NaN if not IsFinite[X]. |
| Tan | Returns the tangent of X, where X is interpreted as a value in radians, if IsFinite[X]. Returns NaN if not IsFinite[X]. |
| ArcSin | Returns the inverse sine (arcsine) of X as a value in radians if -1.0 <= X <= 1.0. |
| ArcCos | Returns the inverse cosine (arccosine) of X as a value in radians if -1.0 <= X <= 1.0. |
| ArcTan | Returns the inverse tangent (arctangent) of X as a value in radians such that:-PiFloat/2.0 <= ArcTan(x) <= PiFloat/2.0. |
| ArcTan | Returns the angle in radians at the origin between a ray pointing to (X, Y) and the positive X axis such that -PiFloat < ArcTan(Y, X) <= PiFloat. Returns 0.0 if X=0.0 and Y=0.0. |
| Sinh | Returns the hyperbolic sine of X. |
| Cosh | Returns the hyperbolic cosine of X. |
| Tanh | Returns the hyperbolic tangent of X. |
| ArSinh | Returns the inverse hyperbolic sine of X if IsFinite(X). |
| ArCosh | Returns the inverse hyperbolic cosine of X if 1.0 <= X. |
| ArTanh | Returns the inverse hyperbolic tangent of X if IsFinite(X). |
| Pow | Returns A to the power of B. |
| Quotient | Returns the quotient X/Y as defined by Euclidean division, i.e.: Quotient[X/Y] = Floor[X/Y] when Y > 0 Quotient[X/Y] = Ceil[X/Y] when Y < 0 Quotient[X/Y] * Y + Mod[X,Y] = X Fails if Y = 0. |
| Mod | Returns the remainder of X/Y as defined by Euclidean division, i.e.: Mod[X,Y] = X - Quotient(X/Y)*Y 0 <= Mod[X,Y] < Abs(Y) Fails if Y=0. |
| Exp | Returns the natural exponent of X. |
| Ln | Returns the natural logarithm of X. |
| Log | Returns the base B logarithm of X. |
| Lerp | Used to linearly interpolate/extrapolate between From (when Parameter = 0.0) and To (when Parameter = 1.0). Expects that all arguments are finite. Returns From*(1 - Parameter) + To*Parameter. |
| Sgn | Returns the sign of Val: 1 if Val > 0 0 if Val = 0 -1 if Val < 0 |
| Sgn | Returns the sign of Val: 1.0 if Val > 0.0 0.0 if Val = 0.0 -1.0 if Val < 0.0 NaN if Val = NaN |
| IsAlmostEqual | Succeeds if Val1 and Val2 are within AbsoluteTolerance of each other. |
| result | Implemented by classes that provide a result for an operation, which can fail or be successful |
| MakeSuccess |  |
| MakeError |  |
| signalable | A parametric interface implemented by events with a payload that can be signaled. Can be used with awaitable, subscribable, or both (see: listenable). |
| Join | Makes a string by concatenating Separator between the elements of Strings. |
| ToString | Returns String without modification. |
| ToString | Makes a string from Character. |
| subscribable | A parametric interface implemented by events with a payload that can be subscribed to. Matched with signalable. |
| subscribable | A parameterless interface implemented by events that can be subscribed to. |
| modifier | Implemented by classes to provide a method for modification evaluation. |
| modifier_stack | Modifier stacks provide an ordered application of modifiers. |

## Data
| Name | Description |
| Inf |  |
| NaN |  |
| PiFloat |  |
