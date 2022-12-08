import os


def init_config(app):
    app.config.from_object("config.default")
    profile = os.environ.get("PYTHON_ENV")
    if profile == "test":
        app.config.from_object("config.test")
    elif profile == "production":
        app.config.from_object("config.production")
