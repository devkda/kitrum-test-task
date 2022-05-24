"""
This module contains package-wide helper functions.
"""
import uuid


def short_random_string():
    return str(uuid.uuid4())[:8]
