"""
This module contains the data transfering objects with
type validation that represents the domain objects.
"""

from typing import List
from datetime import date

from pydantic import BaseModel


class Entry(BaseModel):
    """Single entry with main sales data."""
    department: str
    date: date
    sales: int


class Entries(BaseModel):
    """Container for sales entries."""
    data: List[Entry]
