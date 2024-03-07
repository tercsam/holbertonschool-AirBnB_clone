#!/usr/bin/python3
"""Module that defines City class, inherits from BaseModel."""

from models.base_model import BaseModel


class City(BaseModel):
    """City class initialization."""
    state_id = ""
    name = ""
