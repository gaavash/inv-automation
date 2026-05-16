import sqlite3
import pandas as pd


class DatabaseManager:
    """
    Handles SQLite database operations.
    """

    def __init__(self, db_name="montflow.db"):

        self.db_name = db_name

    def connect(self):
        """
        Create database connection.
        """

        return sqlite3.connect(self.db_name)

    def create_inventory_table(self):
        """
        Create inventory analysis table.
        """

        conn = self.connect()

        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS inventory_analysis (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            product_id INTEGER,
            product_name TEXT,
            category TEXT,

            current_stock INTEGER,
            reorder_level INTEGER,

            weekly_sales INTEGER,
            weeks_of_inventory REAL,

            stockout_risk TEXT,
            overstock_risk TEXT,
            inventory_status TEXT,

            recommended_reorder_qty INTEGER,
            recommendation TEXT
        )
        """)

        conn.commit()

        conn.close()

        print("Inventory table created")

    def save_analysis_to_database(self, df):
        """
        Save analysis dataframe into database.
        """

        conn = self.connect()

        # Only keep columns that exist in SQL table
        allowed_columns = [

            "product_id",
            "product_name",
            "category",

            "current_stock",
            "reorder_level",

            "weekly_sales",
            "weeks_of_inventory",

            "stockout_risk",
            "overstock_risk",
            "inventory_status",

            "recommended_reorder_qty",
            "recommendation"
        ]

        cleaned_df = df[allowed_columns]

        cleaned_df.to_sql(
            "inventory_analysis",
            conn,
            if_exists="append",
            index=False
        )

        conn.close()

        print("Analysis saved to database")
    
    def load_inventory_data(self):
        """
        Load inventory data from database.
        """

        conn = self.connect()

        query = """
        SELECT * FROM inventory_analysis
        """

        df = pd.read_sql(query, conn)

        conn.close()

        return df
