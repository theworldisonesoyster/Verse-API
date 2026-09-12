Modifier stacks provide an ordered application of modifiers.
|  |  |
| Verse using statement | using { /Verse.org/Verse } |

## Exposed Interfaces
This class exposes the following interfaces:
| Name | Description |
| modifier(t) | Implemented by classes to provide a method for modification evaluation. |

## Members
This class has both data members and functions.

### Data
| Data Member Name | Type | Description |
| FirstPosition | ?rational |  |
| LastPosition | ?rational |  |

### Functions
| Function Name | Description |
| Evaluate | Returns a t which is the input evaluated against each modifier in the stack, executed in position order. |
| AddModifier | Insert a Modifier at Position in the stack. If multiple modifiers are added at the same position, they are applied such that the most recently added is the last evaluated. Returns a cancelable which can be used to remove Modifier from the stack. |
