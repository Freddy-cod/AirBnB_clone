#!/usr/bin/python3
"""User class. Imports Base Model"""
from models.base_model import BaseModel


class User(BaseModel):
    """Manage user objects"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
