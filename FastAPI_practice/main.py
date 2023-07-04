from fastapi import FastAPI
from typing import List
import numpy as np
import joblib
from pathlib import Path


#load model
ROOT_DIR = Path(__file__).resolve().parent
model_path = ROOT_DIR / 'model_v0.pkl'  

model = joblib.load(model_path)


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
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)