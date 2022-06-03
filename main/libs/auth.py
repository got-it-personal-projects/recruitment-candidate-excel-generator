from flask import request

from main import config
from main.commons.exceptions import InvalidAccessToken, MissingAuthorizationHeader

from . import application_jwttoken


def parse_access_token() -> str:
    """
    Parse the access token sent in the authorization header of the request.
    The value of the header should be in the following format:
        Authorization: Bearer <access_token>
    """
    # Check if the Authorization header was provided, if not then return an error
    if "Authorization" not in request.headers:
        raise MissingAuthorizationHeader

    authorization = request.headers["Authorization"]

    # The value of the Authorization header must start with Bearer
    if not authorization.startswith("Bearer "):
        raise InvalidAccessToken

    return authorization[len("Bearer ") :]


def validate_access_token(access_token: str):
    decoded = application_jwttoken.decode(
        access_token,
        secret=config.APPLICATION_SECRET,
        verify=False,
    )
    if not decoded:
        raise InvalidAccessToken

    application_key = decoded.get("iss")
    if application_key != config.APPLICATION_KEY:
        raise InvalidAccessToken

    # It's time to verify the token since we have the application secret
    decoded = application_jwttoken.decode(
        access_token,
        secret=config.APPLICATION_SECRET,
        verify=True,
    )
    if not decoded:
        raise InvalidAccessToken
