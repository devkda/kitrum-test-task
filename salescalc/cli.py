"""
This module contains the command line interface to perform calculations on sales data.
"""

from typing import Optional
from pathlib import Path

import typer

from salescalc.usecases import calculate_total_sales, save_sales_to_csv
from salescalc.utils import short_random_string
from salescalc.settings import settings


cliapp = typer.Typer()


@cliapp.command()
def calculate(
    src: Path, 
    dest: Optional[Path] = typer.Option(None), 
    workers: Optional[int] = typer.Option(settings.workers)
):
    """Command line interface for salescalc."""
    if dest is None:
        dest = short_random_string() + '_' + src.name

    typer.echo(f"Calculating sales from file: {src}, using {workers} workers.")
    result = calculate_total_sales(src, workers)

    save_sales_to_csv(result, dest)
    typer.echo(f"Saved results to file: {dest}")

    typer.echo(result)
