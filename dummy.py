from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

response = client.post("/input", json={"data": "Hi"})

print(response)
