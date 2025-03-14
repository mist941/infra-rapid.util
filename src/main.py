from typing import Optional

import click

from src import __version__


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
def setup(pattern: Optional[str] = None):
    """Use --pattern or -p for infrastructure setup."""
    if pattern is None:
        click.echo("No pattern specified. Use --pattern or -p to specify a pattern.")
        return

    if pattern == "MERN":
        click.echo("Setting up infrastructure with the MERN pattern...")


if __name__ == "__main__":
    cli()
