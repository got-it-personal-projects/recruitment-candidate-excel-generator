import os
import sys

import pytest

from main import app as _app
from main import config
from main.libs.application_jwttoken import encode

from .helpers.client import CustomClient

if os.getenv("ENVIRONMENT") != "test":
    print('Tests should be run with "ENVIRONMENT=test"')
    sys.exit(1)


@pytest.fixture(scope="session", autouse=True)
def app():
    ctx = _app.test_request_context()
    ctx.push()

    yield _app

    ctx.pop()


@pytest.fixture(scope="function", autouse=True)
def client(app):
    app.test_client_class = CustomClient
    token = encode(config.APPLICATION_KEY, config.APPLICATION_SECRET)

    return app.test_client(token=token)
