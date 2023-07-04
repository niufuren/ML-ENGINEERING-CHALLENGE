from diabete_prediction_model.utils.simple_linear_regr_utils import generate_data
import pytest

@pytest.fixture()
def sample_input_data():
    x_train, y_train, x_test, y_test = generate_data()
    return x_train, y_train, x_test, y_test