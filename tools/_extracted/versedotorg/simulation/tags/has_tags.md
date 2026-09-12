An interface representing a mutable collection of tags.
|  |  |
| Verse using statement | using { /Verse.org/Simulation/Tags } |

## Members
This interface has functions, but no data members.

### Functions
| Function Name | Description |
| AddTag | Adds a tag instance to this container. Returns a tag_key that is uniquely associated with the added instance. |
| RemoveTag | Removes the tag instance associated with the tag_key, succeeds if an instance was removed, fails otherwise. |
| RemoveAllTags | Removes all tag instances of type tag_type, succeeds if at least one instance was removed, fails otherwise. |
| RemoveAllTagsExcept | Removes all tag instances that are not of type tag_type, succeeds if at least one instance was removed, fails otherwise. |
| RemoveAllTagsExcept | Removes all tag instances that are not of any of the types in tag_types, succeeds if at least one instance was removed, fails otherwise. |
| ContainsTag | Succeeds if at least one tag of type tag_type is found in this container, fails otherwise. |
| ContainsAllTags | Fails if at least one type in tag_types cannot be found in this container, succeeds otherwise. Note that this means that if tag_types is empty this call succeeds. |
| ContainsAnyTag | Succeeds if at least of the types in tag_types is found in this container, fails otherwise. Note that this means that if tag_types is empty this call fails. |
