import sqlite3

DATABASE = "database.db"


def get_connection():
    connection = sqlite3.connect(DATABASE)

    connection.row_factory = sqlite3.Row

    connection.execute("PRAGMA foreign_keys = ON")

    return connection


def initialize_database():
    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS competitors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            store_name TEXT,
            shop_url TEXT,
            status TEXT NOT NULL DEFAULT 'active',
            date_added TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            competitor_id INTEGER NOT NULL,
            name TEXT NOT NULL,
            category TEXT,
            product_url TEXT,
            status TEXT NOT NULL DEFAULT 'active',
            date_added TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,

            FOREIGN KEY (competitor_id)
                REFERENCES competitors(id)
                ON DELETE CASCADE
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS performance (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_id INTEGER NOT NULL,
            record_date TEXT NOT NULL,
            estimated_revenue REAL NOT NULL DEFAULT 0,
            sales_volume INTEGER NOT NULL DEFAULT 0,

            FOREIGN KEY (product_id)
                REFERENCES products(id)
                ON DELETE CASCADE
        )
    """)

    connection.commit()

    connection.close()