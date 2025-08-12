# Time Series Forecasting for Portfolio Management Optimization

## Project Overview

This project focuses on applying time series forecasting techniques and portfolio optimization strategies to improve investment decisions for Guide Me in Finance (GMF) Investments. Using historical financial data from Tesla (TSLA), Vanguard Total Bond Market ETF (BND), and S&P 500 ETF (SPY), we build predictive models to forecast market trends, optimize portfolio allocation based on these forecasts, and backtest strategies against benchmarks.

---

## Task 1: Preprocess and Explore Financial Time Series Data

### Overview

Download, clean, and explore historical financial data for three key assets to understand data characteristics and prepare for modeling:

- **TSLA:** High-return potential, high volatility.
- **BND:** Low-risk, stable bond ETF.
- **SPY:** Broad market ETF with moderate risk.

### Data Extraction

- **Source:** Yahoo Finance via the `yfinance` Python package.
- **Period:** July 1, 2015 – July 31, 2025.
- Downloaded daily OHLCV (Open, High, Low, Close, Volume) data and computed derived metrics.

### Data Cleaning and Preprocessing

- Ensured correct data types and handled missing data with interpolation or forward fill.
- Aligned data to trading calendar business days.
- Created additional features such as daily returns, rolling volatility, and rolling means.

### Exploratory Data Analysis (EDA)

- Visualized price trends and volatility.
- Detected outliers and unusual return events.
- Conducted stationarity tests (ADF test) to guide modeling approach.

### Key Insights

- Tesla exhibits significant growth and volatility.
- BND provides stability.
- Price series mostly non-stationary; returns more stationary.

### Usage

See `notebooks/01_task1_preprocess_explore.ipynb` for step-by-step walkthrough.

---

## Task 2: Develop Time Series Forecasting Models

### Overview

Build and compare forecasting models to predict Tesla stock prices:

- **ARIMA/SARIMA:** Classical statistical approach.
- **LSTM:** Deep learning model for sequential data.

### Approach

- Chronologically split data into training (2015-2023) and testing (2024-2025).
- Use grid search and `auto_arima` for parameter tuning in ARIMA.
- Design LSTM architecture, tune epochs and batch sizes.
- Evaluate models using MAE, RMSE, and MAPE metrics.

### Key Results

- Forecasts generated for test period.
- Model comparison showing trade-offs between complexity and performance.

### Usage

See `notebooks/02_task2_modeling.ipynb` for detailed model building and evaluation.

---

## Task 3: Forecast Future Market Trends

### Overview

Use the best-performing forecasting model to generate 6-12 month price forecasts for Tesla.

### Forecasting

- Produce future price predictions with confidence intervals.
- Visualize forecasts alongside historical data.

### Interpretation

- Analyze trend direction and pattern anomalies.
- Assess forecast uncertainty via confidence interval width.
- Discuss market opportunities and risks implied by forecasts.

### Usage

See `notebooks/03_task3_forecast_analysis.ipynb`.

---

## Task 4: Optimize Portfolio Based on Forecast

### Overview

Use forecasted returns for Tesla combined with historical returns for BND and SPY to construct an optimized portfolio using Modern Portfolio Theory (MPT).

### Steps

- Compute expected returns vector: forecasted Tesla returns + historical averages for BND, SPY.
- Calculate covariance matrix of daily returns for all assets.
- Generate Efficient Frontier portfolios.
- Identify and mark:
  - Maximum Sharpe Ratio Portfolio (Tangency portfolio).
  - Minimum Volatility Portfolio.
- Select and justify an optimal portfolio based on risk-return preferences.

### Summary

Provide portfolio weights, expected annual return, volatility, and Sharpe ratio.

### Usage

See `notebooks/04_task4_portfolio_optimization.ipynb`.

---

## Task 5: Strategy Backtesting

### Overview

Validate portfolio strategy by simulating its performance over the most recent year and compare against a benchmark.

### Methodology

- Backtesting period: August 1, 2024 – July 31, 2025.
- Benchmark: Static 60% SPY / 40% BND portfolio.
- Strategy portfolio: Optimal weights from Task 4 (or Tesla-only simplified version).
- Hold weights fixed for the year (no monthly rebalancing for simplicity).
- Calculate cumulative returns and risk-adjusted metrics (Sharpe ratio).

### Results

- Plot cumulative returns of strategy vs. benchmark.
- Summarize total return and Sharpe ratio.
- Discuss strategy viability based on performance.

### Usage

See `notebooks/05_task5_backtesting.ipynb`.

---

## Project Dependencies

- Python 3.8+
- pandas
- numpy
- matplotlib
- seaborn
- yfinance
- statsmodels
- pmdarima
- tensorflow / keras (for LSTM)
- PyPortfolioOpt (for portfolio optimization)

### Install dependencies using:

```bash
pip install -r requirements.txt
