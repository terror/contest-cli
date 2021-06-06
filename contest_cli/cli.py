"""parse command line arguments"""
# pylint: disable=W0622
# pylint: disable=no-value-for-parameter

import sys
import click
from contest_cli.client import Client
from contest_cli.display import Display
from contest_cli.constants import SITES


@click.command()
@click.option(
  "--site",
  "-s",
  required=False,
  help="Programming contest website name"
)
@click.option(
    "--list",
    "-l",
    required=False,
    default=False,
    is_flag=True,
    help="View supported contest websites",
)
def cli(site, list):
  """cli entry point"""

  client = Client()

  if site:
    if site.lower() not in SITES:
      click.secho("Error: Invalid site name.", err=True, fg="red")
      sys.exit(1)
    Display.site(client.get(f"/{SITES[site.lower()]}"))

  if list:
    Display.list(SITES.keys())


if __name__ == "__main__":
  cli()
