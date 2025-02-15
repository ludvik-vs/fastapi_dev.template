from sqlalchemy.orm import Session
from app.repositories.test_repository import TestRepository
from app.schemas.test_schema import TestResponse

def get_test_data(db: Session) -> TestResponse:
    """
    Lógica de negocio para obtener datos de prueba.
    """
    repository = TestRepository(db)
    return repository.get_test_data()
