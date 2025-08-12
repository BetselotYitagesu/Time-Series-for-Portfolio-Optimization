"""
Minimal forecasting functions using only statsmodels & numpy.
No PyTorch dependency.
"""

from typing import Tuple
import numpy as np
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA


def arima_forecast(
    df: pd.DataFrame,
    column: str,
    order: Tuple[int, int, int] = (5, 1, 0),
    steps: int = 30
) -> pd.DataFrame:
    """ARIMA forecast with confidence intervals."""
    series = df[column].astype(float)
    model = ARIMA(series, order=order)
    fit = model.fit()
    forecast_res = fit.get_forecast(steps=steps)
    forecast_df = forecast_res.summary_frame()

    last_date = df.index[-1]
    future_dates = [
        last_date + pd.Timedelta(days=i)
        for i in range(1, steps + 1)
    ]
    forecast_df.index = future_dates
    return forecast_df


def moving_average_forecast(
    df: pd.DataFrame,
    column: str,
    steps: int = 30,
    window: int = 5
) -> pd.DataFrame:
    """Simple moving average forecast."""
    series = df[column].astype(float)
    avg = series.rolling(window=window).mean().iloc[-1]
    preds = np.full(steps, avg)

    last_date = df.index[-1]
    future_dates = [
        last_date + pd.Timedelta(days=i)
        for i in range(1, steps + 1)
    ]
    return pd.DataFrame({"predicted_mean": preds}, index=future_dates)
