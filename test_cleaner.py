from utils.data_cleaner import DataCleaner
from logic.inventory_analysis import InventoryAnalyzer


# Initialize classes
cleaner = DataCleaner()
analyzer = InventoryAnalyzer()


# Load and clean inventory data
inventory_df = cleaner.clean_data("data/inventory.csv")


# Load and clean sales data
sales_df = cleaner.clean_data("data/sales.csv")


# Analyze inventory
analysis_df = analyzer.analyze_inventory(
    inventory_df,
    sales_df
)


print("\nInventory Analysis Results:\n")

print(
    analysis_df[
        [
            "product_name",
            "current_stock",
            "weekly_sales",
            "weeks_of_inventory",
            "stockout_risk",
            "overstock_risk",
            "inventory_status"
        ]
    ]
)
