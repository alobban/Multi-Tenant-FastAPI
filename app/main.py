from fastapi import FastAPI, Depends, HTTPException
from uuid import uuid4
from fastapi.responses import RedirectResponse
import requests
from sqlalchemy import select

from db import get_db
from models import Tenant, User
from schema_types import TenantCreate, TenantOut, UserCreate, UserOut
from middleware import tenant_middleware, get_tenant_id

app = FastAPI()
app.middleware("http")(tenant_middleware)

@app.get("/login")
def login():
    return RedirectResponse(
        'https://dev-lobban876.us.auth0.com/authorize'
        '?response_type=code'
        '&client_id=lTsc9z3BOROX4Gact75m0LCFkTurp7cb'
        '&redirect_uri=http://localhost:8000/token'
        '&scope=offline_access openid profile email'
        '&audience=https://prommiseme.com/api/tenants'
    )

@app.get("/token")
def get_access_token(code: str):
    payload = (
        "grant_type=authorization_code"
        "&client_id=lTsc9z3BOROX4Gact75m0LCFkTurp7cb"
        "&client_secret=lzKa3VZrlxZiWqHbV1O3kz6A-9zBopHY76E7BCp1FsSDNwjFYoLZ2QpTPdbP2868"
        f"&code={code}"
        "&redirect_uri=http://localhost:8000/token"
    )
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(
        'https://dev-lobban876.us.auth0.com/oauth/token',
        payload,
        headers=headers
    )
    return response.json()

@app.get("/tenants", response_model=list[TenantOut])
async def list_tenants(db=Depends(get_db)):
    q = await db.execute(select(Tenant))
    tenants = q.scalars().all()
    return tenants

@app.post("/tenants", response_model=TenantOut)
async def create_tenant(data: TenantCreate, db=Depends(get_db)):
    tenant = Tenant(id=uuid4(), name=data.name)
    db.add(tenant)
    await db.commit()
    await db.refresh(tenant)
    return tenant

@app.post("/users", response_model=UserOut)
async def create_user(data: UserCreate, tenant_id=Depends(get_tenant_id), db=Depends(get_db)):
    q = await db.execute(select(Tenant).where(Tenant.id == tenant_id))
    if q.scalar_one_or_none() is None:
        raise HTTPException(404, "Tenant not found")
    user = User(id=uuid4(), tenant_id=tenant_id, email=data.email, name=data.name)
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user