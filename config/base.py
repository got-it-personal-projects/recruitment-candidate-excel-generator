import logging


class BaseConfig:
    LOGGING_LEVEL = logging.INFO

    APPLICATION_KEY = "recruitment-tool-key"
    APPLICATION_SECRET = "recruitment-tool-secret"

    SENDER_EMAIL = ""
    RECIPIENT_EMAILS = ""

    SENDGRID_API_KEY = (
        ""
    )
