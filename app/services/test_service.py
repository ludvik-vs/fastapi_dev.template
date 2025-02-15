from app.schemas.test_schema import TestResponse

def get_test_data() -> TestResponse:
    """
    Lógica de negocio para el endpoint de prueba.
    Aquí podrías agregar interacción con la base de datos o lógica adicional.
    """
    return TestResponse(message="Hola desde FastAPI Dev Template!")
