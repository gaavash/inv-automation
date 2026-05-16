import streamlit as st
import pandas as pd

from utils.data_cleaner import DataCleaner
from logic.inventory_analysis import InventoryAnalyzer
from logic.recommendation_engine import RecommendationEngine


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
