from pydantic import BaseModel, EmailStr
from uuid import UUID

class TenantCreate(BaseModel):
    name: str

class TenantOut(BaseModel):
    id: UUID
    name: str

class UserCreate(BaseModel):
    email: EmailStr
    name: str

class UserOut(BaseModel):
    id: UUID
    tenant_id: UUID
    email: EmailStr
    name: str