#!/usr/bin/python3
"""This module defines the 'city class'"""
from models.base_model import BaseModel


class city(BaseModel): 
    state_id = str()
    name = str()
