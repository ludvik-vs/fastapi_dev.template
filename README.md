# fastapi_dev.template

├── app/
│   ├── main.py          # Punto de entrada de la aplicación
│   ├── api/
│   │   └── routes/      # Tus endpoints (por ejemplo, test.py y otros)
│   ├── core/
│   │   └── config.py    # Configuración centralizada (variables de entorno, settings)
│   ├── models/          # Modelos de base de datos
│   ├── schemas/         # Esquemas Pydantic
│   ├── services/        # Lógica de negocio, validaciones y reglas de negocio
│   ├── db/
│   │   ├── session.py   # Manejo de sesiones y conexiones a la BD
│   │   └── base.py      # Base metadata para ORM
│   └── utils/           # Funciones y helpers reutilizables
├── alembic/             # Migraciones
├── alembic.ini
├── requirements.txt
└── README.md

**Create VE Python 3.10**
```py -3.10 -m venv .venv```

**Activate VE**
```.venv\Scripts\activate```

**Install Requirements**
```pip install requirements.txt```

**alembic workflow:**

1. ```alembic init alembic```
2. ```alembic revision -m "Create Users table"```
3. ```alembic upgrade head```