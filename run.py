import os
from dotenv import load_dotenv

from app import create_app
from config import CONFIG_MAP


load_dotenv()

application = create_app()


if __name__ == '__main__':
    application.run(host='127.0.0.1')
    if application.config['DEBUG']:
        application.logger.setLevel('DEBUG')
    else:
        application.logger.setLevel('INFO')
