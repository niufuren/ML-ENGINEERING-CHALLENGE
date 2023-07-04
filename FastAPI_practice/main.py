from fastapi import FastAPI
from typing import List
import numpy as np
import joblib
import uvicorn

#load model
model = joblib.load('./model_v0.pkl')

app = FastAPI()

@app.post("/predict")
async def predict(input: float):
    result = model.predict(input)
    result_show = result.flatten().tolist()

    return {"Response Predict": result_show}

@app.post("/predict_batch")
async def predict_batch(input: List[float]):
    input_transform = np.array(input)[:, np.newaxis]
    result = model.predict(input_transform)
    result_output = result.flatten().tolist()

    return {"Response Predict": result_output}

if __name__ == "__main__":
	uvicorn.run("main:app", host="localhost", port=8000, reload=True)