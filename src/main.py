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
def start():
    """Start the setup process."""
    # Use a dictionary to map languages to their frameworks for better organization
    framework_options = {
        "python": ["fastapi", "flask"],
        "javascript": ["express", "nestjs"],
    }

    frontend_framework = click.prompt(
        "Choose a frontend framework",
        type=click.Choice(framework_options["javascript"], case_sensitive=False),
    )

    backend_language = click.prompt(
        "Choose a backend language",
        type=click.Choice(list(framework_options.keys()), case_sensitive=False),
    )

    backend_framework = click.prompt(
        "Choose a backend framework",
        type=click.Choice(framework_options[backend_language], case_sensitive=False),
    )

    database = click.prompt(
        "Choose a database",
        type=click.Choice(["postgresql", "mysql", "mongodb"], case_sensitive=False),
    )

    click.echo(
        f"You chose {frontend_framework} and {backend_language} with {backend_framework} and {database}!"
    )


@cli.command()
@click.argument("pattern", required=False)
def pattern(pattern: Optional[str] = None):
    """Use a predefined pattern."""
    if pattern is None:
        click.echo("No pattern specified. Available patterns: MERN, PERN, etc.")
        return
    click.echo(f"You chose {pattern}!")


if __name__ == "__main__":
    cli()
