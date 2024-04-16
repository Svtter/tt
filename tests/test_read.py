from svtter_template_creator import lib


def has(dict_o, key):
    return key in dict_o


def test_read():
    config = lib.read_repo()
    assert has(config, "django")


def test_get_dict():
    assert "django" in lib.get_dict()
