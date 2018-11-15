from app import create_app


def test_config_dev():
    app = create_app('dev')
    assert app.config['TESTING'] is not True
    assert app.config['DEBUG'] is True


def test_config_test():
    app = create_app('test')
    assert app.config['TESTING'] is True
    assert app.config['DEBUG'] is True


def test_config_prod():
    app = create_app('prod')
    assert app.config['TESTING'] is not True
    assert app.config['DEBUG'] is not True

