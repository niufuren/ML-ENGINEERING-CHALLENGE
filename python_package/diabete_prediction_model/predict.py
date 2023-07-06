import joblib
from typing import List
from pathlib import Path
import numpy as np

    
ROOT_DIR = Path(__file__).resolve().parent
model_path = ROOT_DIR / 'trained_model/model_v0.0.1.pkl'  

_model = joblib.load(model_path)

def make_prediction(input:List[float]):
    input_data = np.array(input)
    result = _model.predict(input_data)
    return result
