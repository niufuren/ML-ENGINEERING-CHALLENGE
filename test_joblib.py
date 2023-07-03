
import joblib
# import simple_linear_regr
model = joblib.load('./model_v0.pkl')

result = model.predict(2)

print('predict  is ', result)