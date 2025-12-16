# Multitenant template (FastAPI)
Mutlitenant FastAPI is a simplified setup of a multitenant backend REST application using the python framework FastAPI, containerized PostgreSQL, SQL Alchemy, Pydantics 2.

## Steps to setup
- First we need install the packages with the following command:

```bash
pip install -r requirements.txt
```

- Second with Docker Desktop installed and running, we can now load the PostgreSQL DB:

```bash
docker compose up -d
```

- Third you will need to apply the migrations:

```bash
alembic upgrade head
```

Once all is successfully installed and running, you can now run the application server with the following **dev** command:

```bash
uvicorn ./app/main:app --reload
```

**Production**
```bash
fastapi ./app/main.py
```

## Access Documentations
We can access Swagger by routing to `/docs`:

[localhost:8000/docs](http://localhost:8000/docs)

We can access Redocly by routing to `/redoc`:

[localhost:8000/redoc](http://localhost:8000/redoc)

We can access the Open API JSON by routing to `/openapi.json`:

[localhost:8000/openapi.json](http://localhost:8000/openapi.json)
