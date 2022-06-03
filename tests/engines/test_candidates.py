import pytest

from main.engines.candidates import save_candidate
from tests.data.candidates import invalid_candidate, valid_candidate
from tests.helpers.mocks.email import mock_send_email


def test_save_candidate_successfully(mocker):
    mock_send_email(mocker)

    assert save_candidate(valid_candidate) is None


def test_save_candidate_with_missing_data(mocker):
    mock_send_email(mocker)

    with pytest.raises(KeyError):
        save_candidate(invalid_candidate)
