import streamlit as st
import pandas as pd
import plotly.express as px

from utils.data_cleaner import DataCleaner
from logic.inventory_analysis import InventoryAnalyzer
from logic.recommendation_engine import RecommendationEngine
from logic.forecasting import DemandForecaster
from logic.ai_assistant import AIInventoryAssistant
from database.db import DatabaseManager

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(
    page_title="MontFlow AI",
    layout="wide"
)


# ---------------------------------------------------
# INITIALIZE CLASSES
# ---------------------------------------------------

cleaner = DataCleaner()
analyzer = InventoryAnalyzer()
recommendation_engine = RecommendationEngine()
forecaster = DemandForecaster()
ai_assistant = AIInventoryAssistant()
db_manager = DatabaseManager()

db_manager.create_inventory_table()

# ---------------------------------------------------
# TITLE
# ---------------------------------------------------

st.title("📦 MontFlow AI")
st.subheader(
    "Retail Inventory Workflow Automation System"
)


# ---------------------------------------------------
# FILE UPLOADS
# ---------------------------------------------------

st.sidebar.header("Upload Data Files")

inventory_file = st.sidebar.file_uploader(
    "Upload Inventory CSV",
    type=["csv"]
)

sales_file = st.sidebar.file_uploader(
    "Upload Sales CSV",
    type=["csv"]
)


# ---------------------------------------------------
# MAIN LOGIC
# ---------------------------------------------------

if inventory_file and sales_file:

    # Load CSV files
    inventory_df = pd.read_csv(inventory_file)
    sales_df = pd.read_csv(sales_file)

    # Clean data
    inventory_df = cleaner.standardize_column_names(
        inventory_df
    )

    inventory_df = cleaner.fill_missing_values(
        inventory_df
    )

    inventory_df = cleaner.clean_product_names(
        inventory_df
    )

    sales_df = cleaner.standardize_column_names(
        sales_df
    )

    sales_df = cleaner.fill_missing_values(
        sales_df
    )

    # Run analysis
    analysis_df = analyzer.analyze_inventory(
        inventory_df,
        sales_df
    )

    # Generate recommendations
    final_df = recommendation_engine.apply_recommendations(
        analysis_df
    )
    # Run forecasting pipeline
    final_df = forecaster.run_forecast_pipeline(
        final_df
    )
    # Generate AI insights
    ai_insights = ai_assistant.generate_insights(
        final_df
    )
    # Save analysis to database
    db_manager.save_analysis_to_database(final_df)

    # ---------------------------------------------------
    # KPI SECTION
    # ---------------------------------------------------

    st.header("📊 Inventory KPIs")

    total_products = len(final_df)

    reorder_count = len(
        final_df[
            final_df["inventory_status"] ==
            "Reorder Needed"
        ]
    )

    overstock_count = len(
        final_df[
            final_df["inventory_status"] ==
            "Overstock Alert"
        ]
    )

    healthy_count = len(
        final_df[
            final_df["inventory_status"] ==
            "Healthy"
        ]
    )

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Total Products",
        total_products
    )

    col2.metric(
        "Reorder Alerts",
        reorder_count
    )

    col3.metric(
        "Overstock Alerts",
        overstock_count
    )

    col4.metric(
        "Healthy Products",
        healthy_count
    )

    # ---------------------------------------------------
    # INVENTORY TABLE
    # ---------------------------------------------------

    st.header("📋 Inventory Analysis")

    st.dataframe(
        final_df[
            [
                "product_name",
                "current_stock",
                "weekly_sales",
                "weeks_of_inventory",
                "inventory_status",
                "recommendation"
            ]
        ],
        use_container_width=True
    )
    # ---------------------------------------------------
    # VISUAL ANALYTICS
    # ---------------------------------------------------

    st.header("📈 Visual Analytics")

    # Inventory Status Distribution
    status_counts = (
        final_df["inventory_status"]
        .value_counts()
        .reset_index()
    )

    status_counts.columns = [
        "Inventory Status",
        "Count"
    ]

    fig_status = px.pie(
        status_counts,
        names="Inventory Status",
        values="Count",
        title="Inventory Status Distribution"
    )

    st.plotly_chart(
        fig_status,
        use_container_width=True
    )

    # ---------------------------------------------------

    st.subheader("📦 Current Stock Levels")

    fig_stock = px.bar(
        final_df,
        x="product_name",
        y="current_stock",
        color="inventory_status",
        title="Current Stock by Product"
    )

    st.plotly_chart(
        fig_stock,
        use_container_width=True
    )

    # ---------------------------------------------------

    st.subheader("🔥 Weekly Sales Performance")

    fig_sales = px.bar(
        final_df,
        x="product_name",
        y="weekly_sales",
        color="inventory_status",
        title="Weekly Sales by Product"
    )

    st.plotly_chart(
        fig_sales,
        use_container_width=True
    )

    # ---------------------------------------------------

    st.subheader("⏳ Weeks of Inventory Remaining")

    fig_weeks = px.bar(
        final_df,
        x="product_name",
        y="weeks_of_inventory",
        color="inventory_status",
        title="Weeks of Inventory Remaining"
    )

    st.plotly_chart(
        fig_weeks,
        use_container_width=True
    )
    # ---------------------------------------------------
    # AI INVENTORY ASSISTANT
    # ---------------------------------------------------

    st.header("🤖 AI Inventory Assistant")

    for insight in ai_insights:

        st.info(insight)
    # ---------------------------------------------------
    # FORECASTING ANALYTICS
    # ---------------------------------------------------

    st.header("🔮 Demand Forecasting")

    st.dataframe(
        final_df[
            [
                "product_name",
                "weekly_sales",
                "forecast_4_week_demand",
                "projected_stock_4_weeks",
                "future_stock_risk"
            ]
        ],
        use_container_width=True
    )

    # Forecast Chart

    fig_forecast = px.bar(
        final_df,
        x="product_name",
        y="forecast_4_week_demand",
        color="future_stock_risk",
        title="Forecasted 4-Week Demand"
    )

    st.plotly_chart(
        fig_forecast,
        use_container_width=True
    )
    # ---------------------------------------------------
    # DATABASE HISTORY
    # ---------------------------------------------------

    st.header("🗄 Historical Inventory Records")

    historical_df = db_manager.load_inventory_data()

    st.dataframe(
        historical_df.tail(20),
        use_container_width=True
    )
    # ---------------------------------------------------
    # REORDER PRODUCTS
    # ---------------------------------------------------

    st.header("🚨 Products Requiring Reorder")

    reorder_df = final_df[
        final_df["inventory_status"] ==
        "Reorder Needed"
    ]

    st.dataframe(
        reorder_df[
            [
                "product_name",
                "recommended_reorder_qty",
                "recommendation"
            ]
        ],
        use_container_width=True
    )

else:

    st.info(
        "Please upload inventory and sales CSV files."
    )
