from collections import defaultdict
from typing import List, Dict
from datetime import date

from pydantic import BaseModel


class Entry(BaseModel):
    city: str
    date: date
    sales: int


class Entries(BaseModel):
    data: List[Entry]
