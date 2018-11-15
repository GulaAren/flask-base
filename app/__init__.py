import os

from flask import Flask
from dotenv import load_dotenv

from .config import CONFIG_MAP

load_dotenv()

def create_app(conf):
    app = Flask(__name__)
    
    app.config.from_object(CONFIG_MAP.get(conf, 'dev'))
    app.config['SECRET_KEY'] = os.getenv(
        'SECRET_KEY', app.config['SECRET_KEY']
    )
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
        'SQLALCHEMY_DATABASE_URI',
    )

    print(app.config)

    return app
