def test_fail_to_authorize(client):
    client.set_headers(headers={"Authorization": "Bearer invalid"})

    response = client.post("/candidates")

    assert response.status_code == 401
