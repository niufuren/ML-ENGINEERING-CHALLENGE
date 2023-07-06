## A simple linear model to predict diabetes

This package provides a prediction function to predict the interest of response from diabetes patients. 

### Description
The prediction is made based on a simple linear model. The model in inputted with bmi (body mass index) of 
a patient and outputs the possible interest of reponse in one year.

### Dependencies

### Installation
Install the model package to your local environment
```sh
 pip install dist/diabete_prediction_model-0.0.1-py3-none-any.whl
```

### Usage

The model can be called through the code:

```python
from diabete_prediction_model.predict import make_prediction
bmi = [[1], [2]] # a list of bmi is provided
y_predicted = make_prediction(bmi)
print(y_predicted)
```

The output of the code is:
```python
[[1097.92160477]
 [2049.01921627]]
```