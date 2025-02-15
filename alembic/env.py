from logging.config import fileConfig

from sqlalchemy import create_engine
from sqlalchemy import pool

from alembic import context

import os
from dotenv import load_dotenv

# Carga variables de entorno desde .env
load_dotenv()

# Importa modelos SQLAlchemy
from app.models.models import Base  # Asegúrate de importar tu Base de datos

# Cargando configuración
config = context.config
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Cargar Metadata
target_metadata = Base.metadata

#  🔁 Funciones de migración 
def run_migrations_offline() -> None:
    """Ejecutar migraciones en modo 'offline'.

    Esto configura el contexto sólo con una URL
    y no un motor, aunque un motor es aceptable
    aquí también.  Al omitir la creación del motor
    ni siquiera necesitamos que haya una DBAPI disponible.

    Las llamadas a context.execute() emiten la cadena dada a la salida del script.
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Ejecutar migraciones en modo online."""
    
    DATABASE_URL = os.getenv("DATABASE_URL")

    if not DATABASE_URL:
        raise ValueError("❌ ERROR: La variable de entorno DATABASE_URL no está definida.")

    connectable = create_engine(DATABASE_URL, poolclass=pool.NullPool)

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
