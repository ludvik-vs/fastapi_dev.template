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
