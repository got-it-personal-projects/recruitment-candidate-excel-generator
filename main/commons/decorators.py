from functools import wraps

from main.libs.auth import parse_access_token, validate_access_token


def require_application_auth(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        access_token = parse_access_token()
        validate_access_token(access_token)

        return f(*args, **kwargs)

    return decorated_function
