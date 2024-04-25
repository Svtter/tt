import pathlib as p
import typing as t
from collections import namedtuple

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


Config = namedtuple("Config", ["path", "content"])


def get_config() -> Config:
    p.Path.home().joinpath(".config", "tt").mkdir(parents=True, exist_ok=True)
    tt_file = p.Path.home().joinpath(".config", "tt.toml")

    return Config(str(tt_file), tt_file.read_text())
