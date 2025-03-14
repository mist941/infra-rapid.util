from typing import Optional

import click

from src import __version__
from src.technologies.react import install_react


@click.group()
def cli():
    """Fast Infrastructure Setup"""
    pass


@cli.command()
def version():
    """Display the current version of fis."""
    click.echo(f"fis version {__version__}")


@cli.command()
@click.option("--pattern", "-p", help="Specify the pattern name")
@click.option("--name", "-n", help="Specify the project name")
def setup(pattern: Optional[str] = None, name: Optional[str] = None):
    """Use --pattern or -p for infrastructure setup."""
    if pattern is None:
        click.echo("No pattern specified. Use --pattern or -p to specify a pattern.")
        return
    if name is None:
        click.echo("No name specified. Use --name or -n to specify a name.")
        return

    if pattern == "react":
        install_react(name)


if __name__ == "__main__":
    cli()
