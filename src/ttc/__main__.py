import click

from ttc import __version__


@click.group()
def cli():
    pass


@click.command()
@click.option(
    "--name",
    prompt="template name",
    help="The template need to create; django, package, etc.",
)
def create(name):
    """
    create template via name
    """
    import os

    template_dict = {
        "django": "git@gitee.com:beijing_epoch/cookiecutter-django.git",
        "package": "git@gitee.com:beijing_epoch/cookiecutter-pypackage.git",
    }
    template = template_dict[name]
    os.system(f"cookiecutter {template}")


@click.command()
def version():
    """show version information"""
    click.echo(f"ttc version is: {__version__}")


cli.add_command(create)
cli.add_command(version)
