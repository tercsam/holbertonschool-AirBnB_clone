#!/usr/bin/python3
"""Module that defines Review class, inherits from BaseModel."""

from models.base_model import BaseModel


class Review(BaseModel):
    """State Review initialization."""
    place_id = ""
    user_id = ""
    text = ""
