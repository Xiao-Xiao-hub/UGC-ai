"""Timezone boundaries and compatibility with existing stored timestamps."""
import unittest
from datetime import datetime

from common.time_utils import local_iso


class TimestampTests(unittest.TestCase):
    def test_legacy_naive_database_values_are_utc(self):
        self.assertEqual(local_iso(datetime(2026, 1, 15, 12)), "2026-01-15T07:00:00-05:00")

    def test_old_offset_values_preserve_the_instant(self):
        old = datetime.fromisoformat("2026-07-15T20:00:00+08:00")
        actual = local_iso(old)
        self.assertEqual(actual, "2026-07-15T08:00:00-04:00")
        self.assertEqual(datetime.fromisoformat(actual).timestamp(), old.timestamp())

    def test_spring_transition_skips_missing_hour(self):
        self.assertEqual(local_iso(datetime.fromisoformat("2026-03-08T06:59:00+00:00")), "2026-03-08T01:59:00-05:00")
        self.assertEqual(local_iso(datetime.fromisoformat("2026-03-08T07:00:00+00:00")), "2026-03-08T03:00:00-04:00")

    def test_fall_transition_retains_distinct_instants(self):
        self.assertEqual(local_iso(datetime.fromisoformat("2026-11-01T05:30:00+00:00")), "2026-11-01T01:30:00-04:00")
        self.assertEqual(local_iso(datetime.fromisoformat("2026-11-01T06:30:00+00:00")), "2026-11-01T01:30:00-05:00")

    def test_null_remains_null(self):
        self.assertIsNone(local_iso(None))
