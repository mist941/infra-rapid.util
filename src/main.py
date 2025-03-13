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
    frontend = click.prompt(
        "Choose a frontend framework",
        type=click.Choice(["react", "nextjs"], case_sensitive=False),
    )
    backend_language = click.prompt(
        "Choose a backend language",
        type=click.Choice(["python", "javascript"], case_sensitive=False),
    )
    if backend_language == "python":
        backend_framework = click.prompt(
            "Choose a backend framework",
            type=click.Choice(["fastapi", "flask"], case_sensitive=False),
        )
    if backend_language == "javascript":
        backend_framework = click.prompt(
            "Choose a backend framework",
            type=click.Choice(["express", "nestjs"], case_sensitive=False),
        )
    print(
        f"You chose {frontend} and {backend_language} with {backend_framework}!"
    )


@cli.command()
def pattern(pattern=None):
    """Use a predefined pattern."""
    click.echo(f"You chose {pattern}!")


if __name__ == "__main__":
    cli()
