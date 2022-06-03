from flask import jsonify, request
from sendgrid import SendGridException

from main import app
from main.commons.decorators import require_application_auth
from main.commons.exceptions import BadRequest, InternalServerError
from main.engines.candidates import save_candidate


@app.route("/candidates", methods=["POST"])
@require_application_auth
def submit_form():
    try:
        candidate_data = request.get_json()
        save_candidate(candidate_data)
        return jsonify({})
    except KeyError:
        raise BadRequest(error_message="Missing the candidate's information.")
    except SendGridException:
        raise InternalServerError(error_message="Unable to send email to recruiters.")
