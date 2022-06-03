from sendgrid import SendGridAPIClient


def mock_send_email(mocker):
    mocker.patch.object(SendGridAPIClient, "send", return_value=None)
