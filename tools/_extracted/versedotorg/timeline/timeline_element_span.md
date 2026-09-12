A timeline element that spans a range of time.
|  |  |
| Verse using statement | using { /Verse.org/Timeline } |

## Inheritance Hierarchy
This class is derived from timeline_element.
| Name | Description |
| timeline_element | Abstract definition of any element that can be added to a timeline.See timeline_element_point and timeline_element_span. |

## Members
This class has both data members and functions.

### Data
| Data Member Name | Type | Description |
| BeginTime | ?float | The time this span begins. Defaults to 0.0.Must be <> NaN and <= EndTime in order for it to be updated or queriedMay be +/- Inf |
| EndTime | ?float | The time this span ends. Defaults to Inf.Must be <> NaN and >= BeginTime in order for it to be updated or queriedMay be +/- Inf. |

### Functions
| Function Name | Description |
| SetRange | Called to modify the timeline's range by assigning its begin and end times. |
