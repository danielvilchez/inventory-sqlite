# Overview

This software is an Inventory Management System designed to help users keep track of products, their categories, quantities, prices, and the dates they were added. The purpose of building this software is to practice interacting with a SQL Relational Database using Python and to apply CRUD operations in a real-world scenario.

The program integrates with a **SQLite relational database** (`inventory.db`) where all data is stored. It allows users to insert new products and categories, update product quantities, delete products, and query products. The program also includes an **interactive command-line menu** to perform these operations easily.

This project helps strengthen my understanding of relational databases, SQL commands, and Python programming while creating a functional application.

[Software Demo Video](http://youtube.link.goes.here)

# Relational Database

The software uses **SQLite**, a lightweight relational database that stores data in a single `.db` file. SQLite was chosen because it is easy to integrate with Python, requires no server setup, and supports standard SQL commands.

The database contains the following tables:

1. **categories**

   * `id` (INTEGER, Primary Key, Auto Increment)
   * `name` (TEXT, Unique, Not Null)

2. **products**

   * `id` (INTEGER, Primary Key, Auto Increment)
   * `name` (TEXT, Not Null)
   * `category_id` (INTEGER, Foreign Key → categories.id)
   * `quantity` (INTEGER, default 0)
   * `price` (REAL, default 0.0)
   * `added_date` (TEXT, ISO format `YYYY-MM-DD`)

The `products` table uses a foreign key to reference the `categories` table. The program also demonstrates **JOIN queries**, **aggregate functions** (COUNT, SUM, AVG), and includes functionality for **date range filtering**, although this is currently available through code functions rather than directly in the menu.

# Development Environment

* **Operating System:** Windows 11
* **Code Editor:** Visual Studio Code
* **Programming Language:** Python 3.12.0
* **Libraries Used:**

  * `sqlite3` (standard library for SQLite integration)
  * `os` (for handling file paths)
* **Tools:**

  * VS Code Terminal for running Python scripts
  * Git for version control
  * Optional: DB Browser for SQLite to visualize the database

# Useful Websites

* [SQLite Python Tutorial](https://www.sqlitetutorial.net/sqlite-python/)
* [SQLite Official Documentation](https://www.sqlite.org/docs.html)
* [DB Browser for SQLite](https://sqlitebrowser.org/)
* [Python sqlite3 Module](https://docs.python.org/3/library/sqlite3.html)

# Future Work

* Add **input validation** to prevent incorrect data entry (e.g., invalid dates, category IDs).
* Extend the database with additional tables, e.g., suppliers, orders.
* Add menu options for **filtering products by date range** and advanced queries.
* Add **report generation** features (e.g., export inventory summary to CSV).
* Add more **aggregate and statistical queries** for better analytics.
