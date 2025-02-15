from fastapi import APIRouter
from app.services import test_service
from app.schemas.test_schema import TestResponse

router = APIRouter(prefix="/test", tags=["Test"])

@router.get("/", response_model=TestResponse)
def get_test():
    """
    Endpoint de prueba que retorna un mensaje.
    """
    data = test_service.get_test_data()
    return data
