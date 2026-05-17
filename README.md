# 📦 Inv-Automation

Retail Inventory Workflow Automation & Recommendation System

MontFlow AI is a business-focused inventory analytics platform designed to help retailers improve inventory visibility, automate decision-making workflows, forecast demand, and generate intelligent operational recommendations.

Built using Python, pandas, SQL, and Streamlit.

---

# 🚀 Features

## ✅ Data Cleaning Pipeline
- CSV upload support
- Missing value handling
- Duplicate removal
- Product name standardization

## ✅ Inventory Analytics
- Stockout risk analysis
- Overstock detection
- Weeks-of-inventory calculations
- Inventory health monitoring

## ✅ Recommendation Engine
- Automated reorder recommendations
- Overstock action suggestions
- Rule-based business logic

## ✅ Forecasting System
- 4-week demand forecasting
- Projected stock analysis
- Future inventory risk detection

## ✅ AI Inventory Assistant
- Intelligent operational insights
- Automated inventory commentary
- Forecast-driven recommendations

## ✅ Interactive Dashboard
- KPI cards
- Inventory tables
- Forecast charts
- Visual analytics

## ✅ SQLite Database Integration
- Persistent inventory storage
- Historical inventory records
- SQL-based workflow architecture

---

# 🛠 Tech Stack

| Technology | Purpose |
|---|---|
| Python | Backend Logic |
| pandas | Data Processing |
| Streamlit | Dashboard UI |
| SQLite | Database |
| Plotly | Data Visualization |
| SQL | Persistent Storage |

---

# 📊 Dashboard Preview

_Add screenshots here later._

---

# 📂 Project Structure

```bash
montflow-inventory/
│
├── app/
│   └── dashboard.py
│
├── data/
│
├── database/
│   └── db.py
│
├── logic/
│   ├── inventory_analysis.py
│   ├── recommendation_engine.py
│   ├── forecasting.py
│   └── ai_assistant.py
│
├── utils/
│   └── data_cleaner.py
│
├── tests/
│
├── requirements.txt
├── README.md
└── montflow.db
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/gaavash/montflow-inventory.git
cd montflow-inventory
```

## Create Virtual Environment

### Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run Application

```bash
PYTHONPATH=. streamlit run app/dashboard.py
```

---

# 📈 Future Improvements

- Machine learning demand forecasting
- Multi-store inventory management
- Supplier performance analytics
- Automated email alerts
- OpenAI-powered inventory assistant
- PDF/Excel report exports
- Docker deployment
- Cloud database integration

---

# 👨‍💻 Author

Aavash Gurung

Built as a retail workflow automation and intelligent inventory analytics project.
