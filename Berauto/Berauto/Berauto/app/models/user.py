
from app.extensions import db, Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.types import String, Integer
from sqlalchemy import ForeignKey, Column, Table
from typing import List, Optional
from werkzeug.security import generate_password_hash, check_password_hash


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

    email: Mapped[Optional[str]] = mapped_column(String(100))
    phone : Mapped[str] = mapped_column(String(30))
    password_hash: Mapped[str] = mapped_column(String(128))
    
    roles: Mapped[List["Role"]] = relationship(secondary=UserRole, back_populates="users")
    rentals: Mapped[List["Rental"]] = relationship(secondary=UserRental, back_populates="users")

    def set_password(self, password: str):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        return check_password_hash(self.password_hash, password)