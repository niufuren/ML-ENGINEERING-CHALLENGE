# from diabete_prediction_model.predict import make_prediction

# # import predict

# result = make_prediction(2)

# from diabete_prediction_model.simple_linear_regr_utils import generate_data
# X_train, y_train, X_test, y_test = generate_data()

# from  diabete_prediction_model import simple_linear_regr_utils 

# a = simple_linear_regr_utils.generate_data()

from diabete_prediction_model import predict

a = predict.make_prediction([2])

print(a)