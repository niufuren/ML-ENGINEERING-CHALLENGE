from diabete_prediction_model.simple_linear_regr.simple_linear_regr import SimpleLinearRegression
from diabete_prediction_model.utils.simple_linear_regr_utils import generate_data

def test_fit(sample_input_data):
    x_train, y_train, _, _ = sample_input_data
    model = SimpleLinearRegression(iterations=1)
    model.fit(x_train, y_train)
    loss = model.losses

    assert loss[1] < loss[0]