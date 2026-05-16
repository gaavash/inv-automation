class RecommendationEngine:
    """
    Generates inventory recommendations based on business rules.
    """

    def __init__(self):
        pass

    def calculate_reorder_quantity(self, row):
        """
        Calculate suggested reorder quantity.
        """

        if row["inventory_status"] == "Reorder Needed":

            reorder_qty = (
                row["reorder_level"] - row["current_stock"]
            )

            return max(reorder_qty, 0)

        return 0

    def generate_recommendation(self, row):
        """
        Generate recommendation text.
        """

        if row["inventory_status"] == "Reorder Needed":

            qty = self.calculate_reorder_quantity(row)

            return (
                f"Reorder {qty} units immediately"
            )

        elif row["inventory_status"] == "Overstock Alert":

            return (
                "Reduce purchasing or run promotion"
            )

        else:

            return (
                "Inventory level is healthy"
            )

    def apply_recommendations(self, df):
        """
        Apply recommendations to all products.
        """

        df["recommended_reorder_qty"] = df.apply(
            self.calculate_reorder_quantity,
            axis=1
        )

        df["recommendation"] = df.apply(
            self.generate_recommendation,
            axis=1
        )

        print("Generated inventory recommendations")

        return df
