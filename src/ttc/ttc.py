def create(name):
    """
    create template via name
    """
    import os

    template_dict = {
        "django": "git@gitee.com:beijing_epoch/cookiecutter-django.git",
        "package": "git@gitee.com:beijing_epoch/cookiecutter-pypackage.git",
        "compose": "git@gitee.com:beijing_epoch/cookiecutter-compose.git",
    }
    template = template_dict[name]
    os.system(f"cookiecutter {template}")
