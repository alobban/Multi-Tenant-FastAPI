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

Once all is successfully installed and running, you can now run the application server with the following **dev** command:

```bash
uvicorn ./app/main:app --reload
```

**Production**
```bash
fastapi ./app/main.py
```

## Access Swagger
We can access Swagger by routing to `/docs`:

[localhost:8000/docs](http://localhost:8000/docs)
