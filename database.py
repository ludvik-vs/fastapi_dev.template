from sqlalchemy import create_engine, exc
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

# Definir el engine antes de intentar la conexión
engine = None

try:
    if not DATABASE_URL:
        raise ValueError("DATABASE_URL no está definido en las variables de entorno.")

    engine = create_engine(DATABASE_URL, echo=True)  # echo=True muestra consultas en la consola

    # Prueba la conexión a la base de datos
    with engine.connect() as conn:
        print("✅ Conexión a la base de datos exitosa.")

except (exc.SQLAlchemyError, ValueError) as e:
    print(f"❌ Error al conectar a la base de datos: {e}")
    raise  # Propagar el error en lugar de solo imprimirlo

# Solo definir sessionmaker y Base si `engine` se creó correctamente
if engine:
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base = declarative_base()
else:
    raise RuntimeError("No se pudo inicializar la base de datos debido a un error en la conexión.")

def get_db():
    db = SessionLocal()
    print("db session open")
    try:
        yield db
    finally:
        db.close()