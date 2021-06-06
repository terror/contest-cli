import pytest
from contest_cli.utils import Utils


def test_convert_date():
  """simple date conversion test"""

  dates = {
      "2020-08-05T14:35:00.000": "August 05, 2020",
      "2020-08-16T14:35:00.000": "August 16, 2020",
      "2020-08-08T16:00:00.000": "August 08, 2020"
  }

  for date in dates:
    assert Utils.convert_date(date) == dates[date]


def test_duration():
  """simple duration test"""

  durations = {
      3600: "1 hour",
      7200: "2 hours",
  }

  for duration in durations:
    assert Utils.duration(duration) == durations[duration]


def test_url():
  """simple url conversion test"""

  urls = {
      "https://google.com/lol": "lol",
      "https://codeforces.com/contest/1535": "1535",
      "https://leetcode.com/contest/biweekly-contest-54": "biweekly-contest-54"
  }

  for url in urls:
    assert Utils.url(url) == urls[url]
