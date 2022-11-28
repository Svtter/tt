import click

@click.command()
@click.option('--name', prompt="template name", help='The template need to create')
def c(name):
    import os
    template_dict = {
        'django': "git@gitee.com:beijing_epoch/cookiecutter-django.git",
        'package': "git@gitee.com:beijing_epoch/cookiecutter-pypackage.git"
    }
    template = template_dict[name]
    os.system(f'cookiecutter {template}')
