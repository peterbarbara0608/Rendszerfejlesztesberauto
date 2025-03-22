
from app.extensions import db, Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.types import String, Integer
from sqlalchemy import ForeignKey, Column, Table
from typing import List, Optional


UserRole = Table(
    "userroles",
    Base.metadata,
    Column("user_id", ForeignKey("users.id")),
    Column("role_id", ForeignKey("roles.id"))
)

UserRental = Table(
    "userrentals",
    Base.metadata,
    Column("user_id", ForeignKey("users.id")),
    Column("rental_id", ForeignKey("rentals.id"))
)

class User(db.Model):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))

    address_id: Mapped[int] = mapped_column(ForeignKey("addresses.id"))
    address : Mapped["Address"] = relationship(back_populates="user", lazy=True)

    email: Mapped[Optional[str]]
    phone : Mapped[str] = mapped_column(String(30))
    
    roles: Mapped[List["Role"]] = relationship(secondary=UserRole, back_populates="users")
    rentals: Mapped[List["Rental"]] = relationship(secondary=UserRental, back_populates="users")