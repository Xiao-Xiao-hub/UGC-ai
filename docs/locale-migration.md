# Locale and timestamp migration

The interface uses English and displays timestamps in `America/New_York`, including daylight saving time. Database timestamps retain their original instants. Offset-aware legacy timestamps remain readable; naive note timestamps retain the previous interpretation as UTC. No database update is required for note timestamps.

New project and compilation metadata use Eastern offsets. Existing ISO timestamps with other offsets are still valid and must not be replaced by changing their offset text. Artifact filenames include the offset to distinguish the repeated hour in autumn.

The model supplier's peak window remains 08:00–16:00 UTC. It does not follow the user's display timezone.

Existing compiler paths and user-authored notes remain unchanged. Back up application data before deployment.
