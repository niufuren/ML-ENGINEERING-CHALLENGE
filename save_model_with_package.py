import joblib
from diabete_prediction_model.simple_linear_regr.simple_linear_regr import SimpleLinearRegression
from diabete_prediction_model.simple_linear_regr_utils import generate_data, evaluate

if __name__ == "__main__":
    X_train, y_train, X_test, y_test = generate_data()
    model = SimpleLinearRegression()
    model.fit(X_train,y_train)
    predicted = model.predict(X_test)
    evaluate(model, X_test, y_test, predicted)
    # save the model
    # SimpleLinearRegression.__module__ = "model_maker"
    joblib.dump(model, './model_v1.pkl')