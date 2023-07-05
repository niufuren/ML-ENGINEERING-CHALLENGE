import numpy as np
from diabete_prediction_model.predict import make_prediction
from sklearn.metrics import r2_score
from diabete_prediction_model.utils.simple_linear_regr_utils import generate_data

def test_make_prediction(sample_input_data):
    
    expected_no_prediction = 20
    _, _, x_test, y_test = sample_input_data
    y_predicted = make_prediction(x_test)
    assert isinstance(y_predicted, np.ndarray)
    assert len(y_predicted) == expected_no_prediction
    
    r2 = r2_score(y_test, y_predicted)
    assert r2 >= 0.4
    
