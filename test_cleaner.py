from utils.data_cleaner import DataCleaner
from logic.inventory_analysis import InventoryAnalyzer
from logic.recommendation_engine import RecommendationEngine


# Initialize classes
cleaner = DataCleaner()
analyzer = InventoryAnalyzer()
recommendation_engine = RecommendationEngine()


# Load and clean inventory data
inventory_df = cleaner.clean_data("data/inventory.csv")


# Load and clean sales data
sales_df = cleaner.clean_data("data/sales.csv")


# Run inventory analysis
analysis_df = analyzer.analyze_inventory(
    inventory_df,
    sales_df
)


# Generate recommendations
final_df = recommendation_engine.apply_recommendations(
    analysis_df
)


print("\nFinal Inventory Recommendations:\n")

print(
    final_df[
        [
            "product_name",
            "current_stock",
            "weekly_sales",
            "weeks_of_inventory",
            "inventory_status",
            "recommended_reorder_qty",
            "recommendation"
        ]
    ]
)
