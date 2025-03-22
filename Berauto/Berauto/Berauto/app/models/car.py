
from __future__ import annotations

from typing import List
from app.extensions import db, Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, Column, Table
from sqlalchemy.types import String, Integer, Boolean

CarRental = Table(
    "carrentals",
    Base.metadata,
    Column("car_id", ForeignKey("cars.id")),
    Column("rental_id", ForeignKey("rentals.id"))
)

class Car(db.Model):
    __tablename__ = "cars"
    id: Mapped[int] = mapped_column(primary_key=True)
    license: Mapped[str] = mapped_column(String(30))
    model: Mapped[str] = mapped_column(String(30))
    traveled: Mapped[int] = mapped_column(Integer)
    available: Mapped[bool] = mapped_column(Boolean)

    rentals: Mapped[List["Rental"]] = relationship(secondary=CarRental, back_populates="cars")