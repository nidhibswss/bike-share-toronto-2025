# Bike Share Toronto 2025 — Ridership Analysis 🚲 

A full-cycle data analysis project examining **7.8 million trips** from Toronto's Bike Share program across 2025. This project covers data integration, cleaning, feature engineering, exploratory analysis, and interactive visualization.

---

## Dashboard Preview

*Monthly ridership peaks in July (~1.19M trips) and drops sharply in winter months, reflecting Toronto's climate-driven cycling patterns.*

---

## Project Structure

```
bike-share-toronto-2025/
│
├── main.py                              # Data ingestion, cleaning & feature engineering
├── Bike_Share_TO_2025.ipynb             # Exploratory data analysis notebook
├── Bike_share_dashboard_2025.twbx       # Tableau packaged workbook (open in Tableau Desktop/Public)
├── Bike_share_dashboard_2025.png        # Dashboard export preview
└── README.md
```

---

## Key Findings

| Insight of Bike Share Toronto 2025 Rideshare Analysis | Detail |
|---|---|
| Peak month | July (~1.19M trips) |
| Lowest month | February (~130K trips) |
| Busiest hours | 8–9 AM and 5–6 PM |
| Dominant user type | Annual members |

---

## Methodology

### 1. Data Collection & Integration
- Combined **12 monthly CSV files** into a single dataset using Pandas
- Final dataset: ~**7.8 million trip records**

### 2. Data Cleaning
- Standardized column names (lowercase, stripped whitespace)
- Handled encoding issues and skipped malformed rows
- Converted `start_time` and `end_time` to `datetime` format
- Inspected and documented missing values

### 3. Feature Engineering
New columns extracted from `start_time`:
- `month` (1–12)
- `hour` (0–23)
- `day_of_week` (Monday–Sunday)

### 4. Exploratory Data Analysis (EDA)

**Seasonal Trends** — Aggregated trips by month to reveal a strong summer peak and winter trough driven by Toronto weather.
**Hourly Usage Patterns** — Trip volume by hour shows two clear commuter spikes: morning (8–9 AM) and evening (5–6 PM), suggesting the system is heavily used for daily commuting.
**User Type Distribution** — Annual members account for the majority of rides, indicating a loyal, habitual user base rather than tourist-driven demand.

---

## 5. Data Visualization

- **Python** (Matplotlib) — used for EDA charts inside the notebook
- **Tableau** — used for the interactive monthly trend dashboard (dashboard exported above)

> To explore the interactive dashboard, open `Bike_share_dashboard_2025.twbx` in [Tableau Desktop](https://www.tableau.com/products/desktop) or the free [Tableau Public](https://public.tableau.com/) app.

---

##  Tech Stack used: 

- Python, Pandas, Matplotlib,Jupyter Notebook, Tableau

---

## What's Next
A few directions I'd explore with more time:

- Predictive modelling — train a regression model to forecast monthly ridership, which could help the city plan bike availability and rebalancing.
- Interactive dashboard — rebuild the Tableau charts in Plotly. 

---

## Getting Started

```bash
# Clone the repo
git clone https://github.com/nidhibswss/bike-share-toronto-2025.git
cd bike-share-toronto-2025

# Install dependencies
pip install pandas matplotlib jupyter

# 1. Download the 12 monthly CSV files for 2025 from the City of Toronto Open Data Portal
#    and place them in the same folder as main.py

# 2. Run the data cleaning script to combine and process all 12 files
python main.py
# This will generate cleaned_bikeshare_2025.csv in the same directory

# 3. Launch the analysis notebook
jupyter notebook Bike_Share_TO_2025.ipynb
```

> **Note:** The cleaned dataset and raw CSVs are not included in this repo due to file size. To reproduce the analysis, download the 12 monthly CSV files for 2025 from the [City of Toronto Open Data Portal](https://open.toronto.ca/dataset/bike-share-toronto-ridership-data/), then run main.py — it will combine and clean them automatically.

---

## Data Source

[Bike Share Toronto Ridership Data — City of Toronto Open Data](https://open.toronto.ca/dataset/bike-share-toronto-ridership-data/)

