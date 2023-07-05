import pytest
from simple_linear_regr import SimpleLinearRegression
from simple_linear_regr_utils import generate_data
import numpy as np

def test_fit(sample_input_data):
    '''Test fit to dectect if the loss decreases when SGD is implemnted once
    '''
    # Given
    x_train, y_train, _, _ = sample_input_data
    iteration_number = 1
    model = SimpleLinearRegression(iterations=iteration_number)
    # When
    model.fit(x_train, y_train)
    # Then
    loss = model.losses

    assert loss[1] < loss[0]

@pytest.mark.parametrize("x_input, y_exprected", [([1], [2]), ([0, 1], [1, 2])])
def test_predict(x_input, y_exprected):
    '''Test predict to detect if the output as expected
    '''
    # Given
    model = SimpleLinearRegression()
    model.W = 1
    model.b = 1
    # When
    y_predicted = model.predict(x_input)
    #Then
    assert np.array_equal(y_predicted, y_exprected)

    