# src/data_loader.py

from typing import List
import pandas as pd
import yfinance as yf


def load_stock_data(tickers: List[str], start: str, end: str) -> pd.DataFrame:
    """
    Download adjusted close prices for given tickers using auto_adjust.

    Returns a DataFrame with tickers as columns and dates as index.
    """
    data = yf.download(
        tickers,
        start=start,
        end=end,
        progress=False,
        auto_adjust=True,  # Adjusted prices (dividends and splits factored in)
        group_by='ticker'
    )

    # If multiple tickers, data columns are MultiIndex: ticker -> OHLCV
    if isinstance(data.columns, pd.MultiIndex):
        close_df = pd.DataFrame()
        for ticker in tickers:
            close_df[ticker] = data[ticker]['Close']
    else:
        # Single ticker case
        close_df = data['Close'].to_frame()

    close_df.index.name = 'Date'
    return close_df


if __name__ == "__main__":
    # Quick test
    tickers = ["TSLA", "BND", "SPY"]
    start = "2015-07-01"
    end = "2025-07-31"
    df = load_stock_data(tickers, start, end)
    print(df.head())
    print(df.tail())
