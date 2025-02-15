**Crea el entorno virtual con la versión específica Python**
```py -3.10 -m venv .venv```

```.venv\Scripts\activate```

**Instalar Paquetes**
```pip install fastapi alembic sqlalchemy psycopg2  python-dotenv pydantic uvicorn pydantic-settings```


**Requirements**
```pip freeze > requirements.txt```

**Comandos básicos FastAPI:**

* ```uvicorn main:app --reload``` Ejecuta la aplicación FastAPI.

* ```uvicorn app.main\:app --reload```

**.env**

```DATABASE_URL=postgresql+psycopg2://user:pass@hos:port/dbname```

```
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

**Ejemplo de flujo de trabajo:**

1. ```alembic init alembic```
2. ```alembic revision -m "Crear tabla de usuarios"```
3. ```alembic upgrade head```

**Comandos básicos alembic:**
* ```alembic init <nombre_directorio>```: Inicializa Alembic en tu proyecto, creando un directorio para las migraciones y un archivo de configuración.
* ```alembic revision --autogenerate -m "Verificando modelos"```: Crea una nueva revisión de migración con un mensaje descriptivo.
* ```alembic upgrade head```: Aplica todas las migraciones pendientes a la base de datos.
* ```alembic downgrade```: Revierte la última migración aplicada.
* ```alembic history```: Muestra el historial de migraciones.

**Comandos adicionales:**

* ```alembic current```: Muestra la revisión actual de la base de datos.
* ```alembic stamp head```: Marca la base de datos como actualizada a la última revisión.
* ```alembic stamp <revisión>```: Marca la base de datos como actualizada a una revisión específica.
* ```alembic branches```: Muestra las ramas de migración.
* ```alembic merge```: Fusiona dos o más ramas de migración.



