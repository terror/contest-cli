"""all display related logic"""

from rich.console import Console
from rich.table import Table
from rich.text import Text
from contest_cli.constants import COL
from contest_cli.utils import Utils
from typing import List


class Display:
    """displays information to the terminal"""

    @staticmethod
    def site(data: List[dict]):
        """displays a single contest websites information"""
        console = Console()

        table = Table(show_header=True, header_style="green")

        for col in COL:
            table.add_column(col)

        for piece in data:
            table.add_row(
                piece["name"],
                Text(Utils.url(piece["url"]), style=f'link {piece["url"]}'),
                Utils.convert_date(piece["start_time"][:-1]),
                Utils.convert_date(piece["end_time"][:-1]),
                Utils.duration(int(piece["duration"])),
            )

        console.print(table)

    @staticmethod
    def list(sites: List[str]):
        """displays a list of supported contest websites"""
        console = Console()

        table = Table(show_header=True, header_style="green")

        table.add_column("Supported Sites", width=15)

        for site in sites:
            table.add_row(site)

        console.print(table)
