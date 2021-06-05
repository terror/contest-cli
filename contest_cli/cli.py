"""parse command line arguments"""

import click
from contest_cli.client import Client
from contest_cli.display import Display
from contest_cli.constants import SITES


@click.command()
@click.option("--site", "-s", required=False, help="Programming contest website name")
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
        Display.site(client.get(f"/{SITES[site]}"))

    if list:
        Display.list(SITES.keys())


if __name__ == "__main__":
    cli()
