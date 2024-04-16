import tomli
import pathlib
import os


def get_dict():
    prefix = os.getenv("TC_URL", "git@github.com:svtter")

    template_dict = {
        "django": "{prefix}/cookiecutter-django.git".format(prefix=prefix),
        "package": "{prefix}/cookiecutter-pypackage.git".format(prefix=prefix),
        "compose": "{prefix}/cookiecutter-compose.git".format(prefix=prefix),
    }
    return template_dict


def create(name):
    """
    create template via name
    """
    template_dict = get_dict()

    template = template_dict[name]
    os.system(f"cookiecutter {template}")


def read_repo():
    c_path = pathlib.Path.home() / ".config" / "tt.toml"
    with open(c_path, "rb") as fp:
        config = tomli.load(fp)

    return config["repos"]
