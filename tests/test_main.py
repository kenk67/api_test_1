import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

@pytest.mark.parametrize("input_data, expected_status, expected_response", [
    ("Hi", 200,  {"message": "Hello"}),  # Assuming no specific response for "Hi" in original code
    ("What", 200, {"message": "What is it ?"}),
    ("Something else", 200, {"message": "Noo input"})
])
def test_input_responses(input_data, expected_status, expected_response):
    response = client.post("/input", json={"data": input_data})

    # Check status code
    assert response.status_code == expected_status

    # For cases where there's an expected response
    if expected_response:
        assert response.json() == expected_response

# Optionally, for debugging purposes, add:
# pytest --capture=no to display prints in pytest
