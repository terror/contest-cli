"""api request client"""

import sys
import click
import requests


class Client:
  """kontests api request client"""

  def __init__(self, url: str = "https://kontests.net/api/v1"):
    self.url = url

  def get(self, query: str) -> dict:
    """performs a get request with `url`"""
    try:
      res = requests.get(self.url + f"/{query}")
      return res.json()
    except requests.exceptions.RequestException as error:
      click.secho("Error: " + error.response.text, err=True, fg="red")
      sys.exit(1)
