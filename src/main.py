# src/main.py
from db import (
    initialize_db, insert_category, insert_product, get_all_products,
    update_product_quantity, delete_product, products_by_category,
    summary_aggregates, products_added_between, get_categories
)
import datetime

def print_products():
    rows = get_all_products()
    if not rows:
        print("No products available.")
        return
    print("All products:")
    for r in rows:
        print(dict(r))

def demo_aggregates():
    agg = summary_aggregates()
    print("Summary:", dict(agg))

def interactive_menu():
    while True:
        print("\nQuick Menu:")
        print("Please make sure to create at least one category before adding products.")
        print("1) View products")
        print("2) Add category")
        print("3) Add product")
        print("4) Update quantity (id, new quantity)")
        print("5) Delete product (id)")
        print("6) Aggregates summary")
        print("7) Exit")
        choice = input("Choose: ")

        # 1) View products
        if choice == "1":
            print_products()

        # 2) Add category
        elif choice == "2":
            cat_name = input("Enter new category name: ")
            insert_category(cat_name)
            print(f"Category '{cat_name}' added.")

        # 3) Add product
        elif choice == "3":
            cats = get_categories()
            if not cats:
                print("No categories available. Please add a category first.")
                continue

            name = input("Name: ")
            print("Existing categories:")
            for c in cats:
                print(f"{c['id']}: {c['name']}")

            # Validación de category_id
            valid_ids = [c['id'] for c in cats]
            while True:
                try:
                    cat_id = int(input("Enter category_id: "))
                    if cat_id in valid_ids:
                        break
                    else:
                        print(f"Invalid category_id. Please choose from existing IDs: {valid_ids}")
                except ValueError:
                    print("Please enter a valid integer.")

            qty = int(input("Quantity: "))
            price = float(input("Price: "))
            date = input("Date (YYYY-MM-DD): ")
            insert_product(name, cat_id, qty, price, date)
            print("Product added.")

        # 4) Update quantity
        elif choice == "4":
            rows = get_all_products()
            if not rows:
                print("No products available. Please add a product first.")
                continue

            print("Existing products:")
            for r in rows:
                print(f"{r['id']}: {r['name']} (Quantity: {r['quantity']})")

            # Validación de product_id
            valid_ids = [r['id'] for r in rows]
            while True:
                try:
                    pid = int(input("Product id: "))
                    if pid in valid_ids:
                        break
                    else:
                        print(f"Invalid product id. Choose from existing IDs: {valid_ids}")
                except ValueError:
                    print("Please enter a valid integer.")

            newq = int(input("New quantity: "))
            update_product_quantity(pid, newq)
            print("Quantity updated.")

        # 5) Delete product
        elif choice == "5":
            rows = get_all_products()
            if not rows:
                print("No products available. Nothing to delete.")
                continue

            print("Existing products:")
            for r in rows:
                print(f"{r['id']}: {r['name']}")

            # Validación de product_id
            valid_ids = [r['id'] for r in rows]
            while True:
                try:
                    pid = int(input("Product id to delete: "))
                    if pid in valid_ids:
                        break
                    else:
                        print(f"Invalid product id. Choose from existing IDs: {valid_ids}")
                except ValueError:
                    print("Please enter a valid integer.")

            delete_product(pid)
            print("Deleted.")


        # 6) Aggregates summary
        elif choice == "6":
            demo_aggregates()

        # 7) Exit
        elif choice == "7":
            print("Exiting program.")
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    initialize_db()
    print("Database initialized. Use the interactive menu to add categories and products.")
    interactive_menu()

#del data\inventory.db
#python src/main.py