import json
import os
from typing import Optional

import click

from src import __version__
from src.generators.project_generator import generate_project


@click.group()
def cli():
    """Fast Infrastructure Setup"""
    pass


@cli.command()
def version():
    """Display the current version of fis."""
    click.echo(f"fis version {__version__}")


@cli.command()
@click.option("--preset", "-p", help="Specify the preset name")
@click.option("--name", "-n", help="Specify the project name")
def setup(preset: Optional[str] = None, name: Optional[str] = None):
    """Use --preset or -p for infrastructure setup."""
    if preset is None:
        click.echo("No preset specified. Use --preset or -p to specify a preset.")
        return
    if name is None:
        click.echo("No name specified. Use --name or -n to specify a name.")
        return

    preset_file = f"src/presets/{preset}.json"
    if not os.path.exists(preset_file):
        click.echo(f"Preset file '{preset_file}' does not exist.")
        return

    with open(preset_file, "r", encoding="utf-8") as file:
        data = json.load(file)
        generate_project(data, name)


if __name__ == "__main__":
    cli()
