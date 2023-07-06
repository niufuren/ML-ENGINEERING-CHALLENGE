from fastapi.testclient import TestClient
import json
from main import app

client = TestClient(app)

def test_stream():
    '''Test the stream API to detect if the response as expected.
    '''
    
    # Given
    response = client.post(
        "/stream", 
        json={"input": 3}
        )

    # When
    result = response.json()['Response Predict']
    
    # Then
    assert len(result) == 1
    
def test_batch():
    '''Test the stream API to detect if the response as expected.
    '''
    # Given
    response = client.post(
        "/batch", 
        json={"input": [3,4]}
        )

    # When
    result = response.json()['Response Predict']
    
    # Then
    assert len(result) == 2
    
