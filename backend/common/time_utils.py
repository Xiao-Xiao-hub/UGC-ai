"""Display timestamps in the configured US Eastern time zone.

Keep stored instants intact. Legacy naive database timestamps represent UTC.
"""
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

DISPLAY_TIMEZONE = ZoneInfo("America/New_York")


def local_iso(value: datetime | None) -> str | None:
    if value is None:
        return None
    if value.tzinfo is None:
        value = value.replace(tzinfo=timezone.utc)
    return value.astimezone(DISPLAY_TIMEZONE).isoformat()
