# app/api/routes/test.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.services import test_service
from app.schemas.test_schema import TestResponse

router = APIRouter(prefix="/test", tags=["Test"])

@router.get("/", response_model=TestResponse)
def get_test(db: Session = Depends(get_db)):
    """
    Endpoint de prueba que retorna un mensaje.
    """
    return test_service.get_test_data(db)
