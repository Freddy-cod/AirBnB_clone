#!/usr/bin/python3
"""Create State class, inhering from Basemodel"""

from models.base_model import BaseModel


class State(BaseModel):
    """Manages your objects(states)"""

    name = ""
