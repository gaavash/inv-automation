class AIInventoryAssistant:
    """
    Generates intelligent inventory insights.
    """

    def __init__(self):
        pass

    def generate_insights(self, df):

        insights = []

        for _, row in df.iterrows():

            product = row["product_name"]

            # Future stock risk
            if row["future_stock_risk"] == "High Risk":

                insights.append(
                    f"⚠️ {product} is projected to stock out within 4 weeks. Immediate replenishment recommended."
                )

            # Overstock risk
            if row["overstock_risk"] == "High":

                insights.append(
                    f"📦 {product} has excess inventory. Consider reducing purchasing or running promotions."
                )

            # Healthy inventory
            if (
                row["inventory_status"] == "Healthy"
                and row["future_stock_risk"] == "Stable"
            ):

                insights.append(
                    f"✅ {product} inventory levels are stable and healthy."
                )

        return insights
