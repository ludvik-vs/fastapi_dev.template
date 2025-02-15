from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.test_routes import test
from app.core.config import settings

app = FastAPI(title=settings.PROJECT_NAME, debug=settings.DEBUG)


# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir rutas
app.include_router(test)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=settings.PORT, reload=True)
