import pathlib as p

default = """[repos]
compose='git@github.com:svtter/cookiecutter-compose.git'
django='git@github.com:svtter/cookiecutter-django.git'
package='git@github.com:svtter/cookiecutter-pypackage.git'
"""


def create_config():
    """
    create a config folder
    """
    p.Path.home().joinpath(".config", "tt").mkdir(parents=True, exist_ok=True)
    tt_file = p.Path.home().joinpath(".config", "tt.toml")

    if tt_file.exists():
        return
    tt_file.write_text(default)
