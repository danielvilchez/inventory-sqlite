# tests/quick_test.py
from src.db import initialize_db, insert_category, insert_product, get_all_products, summary_aggregates

def test_flow():
    initialize_db()
    c = insert_category("Test")
    insert_product("TestItem", c, 3, 2.5, "2025-11-30")
    rows = get_all_products()
    for r in rows:
        print(dict(r))
    print("Added:", dict(summary_aggregates()))

if __name__ == "__main__":
    test_flow()

