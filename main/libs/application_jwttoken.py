# TODO: to be open sourced
import datetime
import os

import jwt


def encode(application_key, application_secret):
    iat = datetime.datetime.utcnow()
    return jwt.encode(
        {
            "iss": application_key,
            "iat": iat,
            "jti": generate_nonce(),
        },
        application_secret,
    )


def decode(access_token, secret=None, verify=True):
    try:
        if verify:
            token = jwt.decode(access_token, secret, algorithms="HS256")
        else:
            token = jwt.decode(
                access_token,
                options={"verify_signature": False},
                algorithms="HS256",
            )
    except jwt.InvalidTokenError:
        return None
    return token


def generate_nonce():
    """
    Generate jti, it is a unique identified
    that is used to prevent the JWT from being replayed.
    """
    return os.urandom(4).hex()
