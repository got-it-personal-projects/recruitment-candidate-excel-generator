from flask import Flask
from flask_cors import CORS
from sendgrid import SendGridAPIClient

from .commons.error_handlers import register_error_handlers
from .config import config

app = Flask(__name__)
app.config.from_object(config)

mail = SendGridAPIClient(config.SENDGRID_API_KEY)

CORS(app)


def register_subpackages():
    import main.controllers  # noqa


register_subpackages()
register_error_handlers(app)
