from tests.data.candidates import invalid_candidate, valid_candidate
from tests.helpers.mocks.email import mock_send_email

request_url = "/candidates"


def test_save_candidate_successfully(client, mocker):
    mock_send_email(mocker)

    response = client.post(request_url, json=valid_candidate)

    assert response.status_code == 200


def test_save_candidate_with_missing_data(client, mocker):
    mock_send_email(mocker)

    response = client.post(request_url, json=invalid_candidate)

    assert response.status_code == 400
