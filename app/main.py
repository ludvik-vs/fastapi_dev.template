from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.test_routes import test
from app.core.config import settings

app = FastAPI(title=settings.PROJECT_NAME, debug=settings.DEBUG)

# app = FastAPI()

ALLOWED_ORIGINS = ["*"] # Permite todos los orígenes (cuidado en producción)

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(test)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=settings.PORT, reload=True)
