from fastapi import FastAPI, Depends, HTTPException, Request
from uuid import uuid4
from fastapi.responses import RedirectResponse
import requests
from sqlalchemy import select

from db import get_db
from models import Tenant, User
from schema_types import TenantCreate, TenantOut, UserCreate, UserOut
from middleware import tenant_middleware, get_tenant_id
from auth_middleware import auth_middleware

app = FastAPI()
app.middleware("http")(tenant_middleware)
app.middleware("http")(auth_middleware)

@app.get("/login")
def login(request: Request):
    return {
        "message": "Authenticated successfully",
        "user": request.state.user
    }
    

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