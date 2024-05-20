from fastapi import FastAPI
from src.controllers.puntosRec_contro import router as puntosRec_router
import uvicorn


app = FastAPI()

app.include_router(puntosRec_router)


if __name__ == '__main__':    
    uvicorn.run("main:app", host="0.0.0.0", port=5000)