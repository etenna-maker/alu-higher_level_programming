#!/usr/bin/python3
"""Defines the City class.

City maps to the cities table of the database and holds a foreign
key pointing at the states table.
"""
from model_state import Base
from sqlalchemy import Column, ForeignKey, Integer, String


class City(Base):
    """Represents a city stored in the cities table."""

    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, nullable=False,
                autoincrement=True, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
