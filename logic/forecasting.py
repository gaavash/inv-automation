class DemandForecaster:
    """
    Handles inventory demand forecasting.
    """

    def __init__(self):
        pass

    def forecast_4_week_demand(self, df):
        """
        Forecast future 4-week demand.
        """

        df["forecast_4_week_demand"] = (
            df["weekly_sales"] * 4
        )

        print("Forecasted 4-week demand")

        return df

    def calculate_projected_stock(self, df):
        """
        Calculate projected stock after 4 weeks.
        """

        df["projected_stock_4_weeks"] = (
            df["current_stock"] -
            df["forecast_4_week_demand"]
        )

        print("Calculated projected stock")

        return df

    def identify_future_stock_risk(self, df):
        """
        Identify future inventory risk.
        """

        df["future_stock_risk"] = df[
            "projected_stock_4_weeks"
        ].apply(
            lambda x:
            "High Risk" if x < 0 else "Stable"
        )

        print("Identified future stock risk")

        return df

    def run_forecast_pipeline(self, df):
        """
        Full forecasting pipeline.
        """

        df = self.forecast_4_week_demand(df)

        df = self.calculate_projected_stock(df)

        df = self.identify_future_stock_risk(df)

        return df
