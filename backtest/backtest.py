"""
This package is designed to handle data with a structured shape of (T, N), where 'T' represents the horizon and 'N' denotes the number of stocks in the index, ensuring compatibility across signal, price, and index composition data.
"""

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

def portfolio_pnl(returns: pd.DataFrame, presence: pd.DataFrame, signal: pd.DataFrame):
    # Avoid lookahead bias by using shift(1)
    pnl = (signal.shift(1) * returns[presence]).sum(axis=1)
    return pnl

def sharpe_ratio(d_returns: pd.Series) -> float:
    return np.sqrt(252) * d_returns.mean() / d_returns.std()

def turnover_in_percent(signal: pd.DataFrame):
    return 100 * signal.diff().abs().sum(axis=1).mean() / signal.abs().sum(axis=1).mean()

def bias_in_bps(d_returns: pd.Series, signal: pd.DataFrame):
    return 10_000 * d_returns.mean() / signal.diff().abs().sum(axis=1).mean()

def book_size(signal: pd.DataFrame):
    return signal.abs().sum(axis=1)

def portfolio_delta(pnl: pd.Series, index_ret: pd.Series):
    data = pd.concat((pnl, index_ret), axis=1)
    data.dropna(inplace=True)
    X = data.iloc[:, 1].values.reshape(-1, 1)
    y = data.iloc[:, 0].values.reshape(-1, 1)
    lr = LinearRegression()
    lr.fit(X, y)
    return lr.coef_[0, 0]

