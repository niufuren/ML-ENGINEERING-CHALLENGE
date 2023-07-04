from diabete_prediction_model.simple_linear_regr.simple_linear_regr import SimpleLinearRegression
from diabete_prediction_model.utils.simple_linear_regr_utils import generate_data

def test_fit(sample_input_data):
    '''Test fit to dectect if the loss decreases when SGD is implemnted once
    '''
    # Given
    x_train, y_train, _, _ = sample_input_data
    iteration_number = 1
    # When
    model = SimpleLinearRegression(iterations=iteration_number)
    model.fit(x_train, y_train)
    # Then
    loss = model.losses

    assert loss[1] < loss[0]

def test_predict():
    pass