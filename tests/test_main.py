from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_input_hi():
    response = client.post("/input", json={"data": "Hi"})
    print(response)

def test_input_what():
    response = client.post("/input", json={"data": "What"})
    assert response.status_code == 200
    assert response.json() == {"message": "What is it ?"}

def test_input_no_data():
    response = client.post("/input", json={"data": "Something else"})
    assert response.status_code == 200
    assert response.json() == {"message": "Noo input"}
