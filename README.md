Task 1 — Preprocess and Explore Financial Data
Overview

This task covers the initial data acquisition, cleaning, and exploratory analysis stages for the Time Series Forecasting for Portfolio Management Optimization project. The goal is to fetch historical financial data for key assets, preprocess the data to ensure quality, and perform exploratory data analysis (EDA) to extract insights for later modeling.
Objectives

    Download historical stock and ETF data for:

        Tesla (TSLA)

        Vanguard Total Bond Market ETF (BND)

        S&P 500 ETF (SPY)

    Clean and preprocess the data:

        Handle missing values and ensure consistent business-day indexing

        Calculate returns, log returns, and rolling volatility

    Conduct exploratory data analysis:

        Visualize price trends and volatility

        Detect outliers and analyze extreme return days

        Test stationarity of price and returns series (Augmented Dickey-Fuller test)

        Calculate key risk metrics such as Value at Risk (VaR) and Sharpe Ratio

Files

    src/data_loader.py
    Contains reusable functions for downloading data using yfinance, preprocessing, and feature engineering.

    notebooks/01_task1_preprocess_explore.ipynb
    Jupyter Notebook demonstrating the end-to-end workflow for Task 1, including data loading, cleaning, EDA visualizations, and statistical tests.

Dependencies

    Python 3.11+ (recommended)

    pandas

    numpy

    yfinance

    matplotlib

    seaborn

    statsmodels

    scipy

Install dependencies via:

pip install pandas numpy yfinance matplotlib seaborn statsmodels scipy

How to Run

    Clone the repo.

    Create a Python virtual environment and install dependencies.

    Run the Jupyter notebook:

jupyter notebook notebooks/01_task1_preprocess_explore.ipynb

    Follow the notebook to reproduce the preprocessing and exploratory analysis.

Notes

    The data covers the period from July 1, 2015, to July 31, 2025.

    Adjusted Close prices are used for all return calculations.

    The notebook and code are structured to allow easy extension for forecasting and portfolio optimization tasks.