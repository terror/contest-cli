import pytest
from contest_cli.client import Client
from contest_cli.constants import SITES


def test_get():
  """fetch all data from all contest sites"""

  client = Client()

  for site in SITES.values():
    data = client.get(f"/{site}")

    for piece in data:
      assert piece["name"]
      assert piece["url"]
      assert piece["start_time"]
      assert piece["end_time"]
      assert piece["duration"]
