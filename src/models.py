# src/models.py
from dataclasses import dataclass

@dataclass
class Category:
    id: int
    name: str

@dataclass
class Product:
    id: int
    name: str
    category_id: int
    quantity: int
    price: float
    added_date: str
