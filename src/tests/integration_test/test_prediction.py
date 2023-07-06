import numpy as np
from sklearn.metrics import r2_score
import joblib
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent.parent
model_path = ROOT_DIR / 'model_v0.pkl'  

model = joblib.load(model_path)


def test_make_prediction(sample_input_data):
    '''Test the model perfromance to detect if model output as expected,
    i.e the data type, the count of data in predicted output and the model performance
    '''
    
    # Given
    expected_no_prediction = 20
    _, _, x_test, y_test = sample_input_data
    
    # When
    y_predicted = model.predict(x_test)
    
    # Then
    assert isinstance(y_predicted, np.ndarray)
    assert len(y_predicted) == expected_no_prediction
    
    r2 = r2_score(y_test, y_predicted)
    assert r2 >= 0.4
    
