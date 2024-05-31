#!/usr/bin/python3
"""All about reviewing"""

from models.base_model import BaseModel


class Review(BaseModel):
    """For management"""

    place_id = ""
    user_id = ""
    text = ""
