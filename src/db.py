# src/db.py
import os
import sqlite3
from sqlite3 import Connection
from typing import List, Tuple, Any

# Construye la ruta absoluta al archivo inventory.db
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "data", "inventory.db")

def get_connection() -> Connection:
    conn = sqlite3.connect(DB_PATH)
    # Para usar filas como dict
    conn.row_factory = sqlite3.Row
    return conn


def initialize_db():
    conn = get_connection()
    cur = conn.cursor()
    # Tabla categories
    cur.execute("""
    CREATE TABLE IF NOT EXISTS categories (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE
    );
    """)
    # Tabla products
    cur.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        category_id INTEGER,
        quantity INTEGER NOT NULL DEFAULT 0,
        price REAL NOT NULL DEFAULT 0.0,
        added_date TEXT, -- ISO date 'YYYY-MM-DD'
        FOREIGN KEY (category_id) REFERENCES categories(id)
    );
    """)
    conn.commit()
    conn.close()

# CRUD: Categories
def insert_category(name: str) -> int:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT OR IGNORE INTO categories (name) VALUES (?);", (name,))
    conn.commit()
    cat_id = cur.lastrowid
    conn.close()
    return cat_id

def get_categories() -> List[sqlite3.Row]:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM categories;")
    rows = cur.fetchall()
    conn.close()
    return rows

# CRUD: Products
def insert_product(name: str, category_id: int, quantity: int, price: float, added_date: str) -> int:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
    INSERT INTO products (name, category_id, quantity, price, added_date)
    VALUES (?, ?, ?, ?, ?);
    """, (name, category_id, quantity, price, added_date))
    conn.commit()
    pid = cur.lastrowid
    conn.close()
    return pid

def update_product_quantity(product_id: int, new_quantity: int):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("UPDATE products SET quantity = ? WHERE id = ?;", (new_quantity, product_id))
    conn.commit()
    conn.close()

def delete_product(product_id: int):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM products WHERE id = ?;", (product_id,))
    conn.commit()
    conn.close()

def get_all_products() -> List[sqlite3.Row]:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT p.*, c.name as category_name FROM products p LEFT JOIN categories c ON p.category_id = c.id;")
    rows = cur.fetchall()
    conn.close()
    return rows

# JOIN example between products and categories (already used in get_all_products)
def products_by_category():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
    SELECT c.name as category, p.name as product, p.quantity, p.price, p.added_date
    FROM products p
    JOIN categories c ON p.category_id = c.id;
    """)
    rows = cur.fetchall()
    conn.close()
    return rows

# Aggregates examples
def summary_aggregates():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) as total_products, SUM(quantity) as total_quantity, AVG(price) as avg_price FROM products;")
    row = cur.fetchone()
    conn.close()
    return row

# Date range query example
def products_added_between(start_date: str, end_date: str) -> List[sqlite3.Row]:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
    SELECT * FROM products
    WHERE added_date BETWEEN ? AND ?
    """, (start_date, end_date))
    rows = cur.fetchall()
    conn.close()
    return rows
