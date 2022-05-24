"""
This module contains the package-wide helper functions.
"""

import uuid


def short_random_string():
    """Generates random short string"""
    return str(uuid.uuid4())[:8]
