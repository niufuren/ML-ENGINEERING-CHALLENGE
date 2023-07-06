from fastapi.testclient import TestClient
import json
from main import app

client = TestClient(app)

def test_stream():
    response = client.post(
        "/stream", 
        json={"input": 3}
        )

    result = response.json()['Response Predict']
    assert len(result) == 1
    
def test_batch():
    payload = json.dumps({"input": (3, 4)})
    response = client.post(
        "/batch", 
        json={"input": [3,4]}
        )

    print(response.json())
    result = response.json()['Response Predict']
    assert len(result) == 2
    
