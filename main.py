from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from routes.test import test

app = FastAPI()

app.include_router(test)

ORIGINS = ["*"] # Permite todos los orígenes (cuidado en producción)

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=ORIGINS,  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    uvicorn.run(app="main:app", host="0.0.0.0", port=8080, reload=True)