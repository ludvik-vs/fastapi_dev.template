from fastapi import APIRouter

test = APIRouter(tags=["Test"])

@test.get("/")
async def root():
    return {"message": "¡Hola desde FastAPI documentation: localhost:8080/docs "}
