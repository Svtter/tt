import click

from ttc import __version__, ttc


@click.group()
def cli():
    pass


@click.command()
@click.option(
    "--name",
    prompt="template name",
    help="The template need to create",
    type=click.Choice(
        [
            "django",
            "package",
        ]
    ),
)
def create(name):
    """
    create template via name
    """
    ttc.create(name)


@click.command()
def version():
    """show version information"""
    click.echo(f"ttc version is: {__version__}")


cli.add_command(create)
cli.add_command(version)
