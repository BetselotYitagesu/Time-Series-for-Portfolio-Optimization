# Task 1: Preprocess and Explore Financial Time Series Data

## Project Overview

This task involves downloading, cleaning, and exploring historical financial data for three key assets to prepare for subsequent modeling:

- **TSLA**: High return potential with high volatility (growth stock).
- **BND**: Low-risk, stable bond ETF.
- **SPY**: Broad market exposure ETF with moderate risk.

The goal is to understand the characteristics of the data, identify patterns, and prepare the dataset for time series modeling in later tasks.

---

## Data Extraction

- Data is sourced from [Yahoo Finance](https://finance.yahoo.com/) using the `yfinance` Python package.
- Historical daily price data (adjusted close prices) is collected for the period from **2015-07-01** to **2025-07-31**.
- Multiple tickers are downloaded simultaneously for efficient data management.

---

## Data Cleaning and Preprocessing

- Ensured all columns have correct data types.
- Checked and handled missing data by forward/backward filling to maintain time series continuity.
- Reindexed data to business days to align with trading calendar.
- Computed additional features:
  - Daily returns and log returns.
  - Rolling volatility and rolling mean with a 21-day window (~1 month).

---

## Exploratory Data Analysis (EDA)

- Visualized adjusted closing prices to identify long-term trends and price behavior.
- Plotted daily percentage changes to analyze volatility and return distribution.
- Calculated rolling statistics to capture short-term fluctuations.
- Conducted outlier detection by highlighting days with unusually high or low returns.
- Performed Augmented Dickey-Fuller (ADF) tests on price and return series to assess stationarity, a critical assumption for time series modeling.

---

## Key Insights

- Tesla’s stock (TSLA) exhibits strong upward trends with pronounced volatility.
- BND offers a much more stable, less volatile return profile.
- SPY tracks the overall market with moderate volatility.
- Stationarity tests reveal that price series are generally non-stationary, requiring differencing for ARIMA modeling.
- Daily returns show varying volatility over time, highlighting periods of market stress and calm.

---

## Usage

- The main data loading and preprocessing functions reside in `src/data_loader.py`.
- The Jupyter notebook `notebooks/01_task1_preprocess_explore.ipynb` contains a step-by-step EDA walkthrough with visualizations and commentary.
- All processed data is saved under the `data/` directory.

---

## Dependencies

- Python 3.8+
- pandas
- numpy
- yfinance
- matplotlib
- seaborn
- statsmodels

Install dependencies with:

```bash
pip install -r requirements.txt
