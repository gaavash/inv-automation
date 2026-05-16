import pandas as pd


class InventoryAnalyzer:
    """
    Handles inventory analysis and business calculations.
    """

    def __init__(self):
        pass

    def merge_inventory_and_sales(self, inventory_df, sales_df):
        """
        Merge inventory and sales data.
        """

        merged_df = pd.merge(
            inventory_df,
            sales_df,
            on="product_id",
            how="left"
        )

        print("Merged inventory and sales data")

        return merged_df

    def calculate_weeks_of_inventory(self, df):
        """
        Calculate how many weeks inventory will last.
        """

        df["weeks_of_inventory"] = (
            df["current_stock"] / df["weekly_sales"]
        ).round(2)

        print("Calculated weeks of inventory")

        return df

    def identify_stockout_risk(self, df):
        """
        Identify products at stockout risk.
        """

        df["stockout_risk"] = df["weeks_of_inventory"].apply(
            lambda x: "High" if x < 1 else "Low"
        )

        print("Identified stockout risks")

        return df

    def identify_overstock_risk(self, df):
        """
        Identify overstocked products.
        """

        df["overstock_risk"] = df["weeks_of_inventory"].apply(
            lambda x: "High" if x > 8 else "Low"
        )

        print("Identified overstock risks")

        return df

    def generate_inventory_status(self, df):
        """
        Generate overall inventory status.
        """

        def get_status(row):

            if row["stockout_risk"] == "High":
                return "Reorder Needed"

            elif row["overstock_risk"] == "High":
                return "Overstock Alert"

            else:
                return "Healthy"

        df["inventory_status"] = df.apply(get_status, axis=1)

        print("Generated inventory status")

        return df

    def analyze_inventory(self, inventory_df, sales_df):
        """
        Full inventory analysis pipeline.
        """

        df = self.merge_inventory_and_sales(
            inventory_df,
            sales_df
        )

        df = self.calculate_weeks_of_inventory(df)

        df = self.identify_stockout_risk(df)

        df = self.identify_overstock_risk(df)

        df = self.generate_inventory_status(df)

        return df
