#!/usr/bin/python3
"""Defines the State class and the Base declarative instance.

State maps to the states table of the database and is the parent
model used by the other scripts of this project.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Represents a state stored in the states table."""

    __tablename__ = "states"
    id = Column(Integer, primary_key=True, nullable=False,
                autoincrement=True, unique=True)
    name = Column(String(128), nullable=False)
