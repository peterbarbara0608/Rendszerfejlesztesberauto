from __future__ import annotations

from typing import List
from app.extensions import db, Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, Column, Table
from sqlalchemy.types import DateTime, Integer

class Rental(db.Model):
    __tablename__ = "rentals"
    id: Mapped[int] = mapped_column(primary_key=True)
    car: Mapped["Car"] = relationship(back_populates="rentals")
    user: Mapped["User"] = relationship(back_populates="rentals")
    start_date: Mapped[DateTime] = mapped_column(DateTime)
    finish_date: Mapped[DateTime] = mapped_column(DateTime)
