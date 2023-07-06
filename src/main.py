from fastapi import FastAPI, APIRouter
from api import api_router

app = FastAPI()
root_router = APIRouter()
app.include_router(api_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)