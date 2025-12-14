from sqlalchemy.orm import declarative_base, Mapped, mapped_column
from sqlalchemy import String, ForeignKey
import uuid

Base = declarative_base()

class Tenant(Base):
    __tablename__ = "tenants"
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String, unique=True)

class User(Base):
    __tablename__ = "users"
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    tenant_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("tenants.id"))
    email: Mapped[str] = mapped_column(String)
    name: Mapped[str] = mapped_column(String)