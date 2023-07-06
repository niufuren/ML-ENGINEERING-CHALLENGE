from fastapi import APIRouter
from typing import List
import numpy as np
import joblib
from pathlib import Path
from pydantic import BaseModel

class StreamInput(BaseModel):
    input: float

class BatchInput(BaseModel):
    input: List[float]

#load model
ROOT_DIR = Path(__file__).resolve().parent
model_path = ROOT_DIR / 'model_v0.pkl'  

model = joblib.load(model_path)

api_router = APIRouter()

@api_router.post("/stream")
async def predict(input: StreamInput):
    result = model.predict(input.input)
    result_show = result.flatten().tolist()

    return {"Response Predict": result_show}

@api_router.post("/batch")
async def predict_batch(input: BatchInput):
    input_transform = np.array(input.input)[:, np.newaxis]
    result = model.predict(input_transform)
    result_output = result.flatten().tolist()

    return {"Response Predict": result_output}