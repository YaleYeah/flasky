from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config
from flask_bootstrap import Bootstrap
from flask_mail import Mail

db = SQLAlchemy()
bootstrap = Bootstrap()
#mail = Mail()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)
    bootstrap.init_app(app)
    #mail.init_app(mail)

    from .main import main
    app.register_blueprint(main,url_prefix="/main")
    return app