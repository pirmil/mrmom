import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import sys
sys.path.append('../')
from backtest.backtest import sharpe_ratio, turnover_in_percent, bias_in_bps, book_size

def cross_section_z_score(df: pd.DataFrame):
    return df.sub(df.mean(axis=1), axis=0).div(df.std(axis=1), axis=0)

def cross_section_normalization(df: pd.DataFrame):
    return df.div(df.abs().sum(axis=1), axis=0)

def compute_metrics(signal: pd.DataFrame, pnl: pd.Series):
    sharpe = sharpe_ratio(pnl)
    turnover = turnover_in_percent(signal)
    bias = bias_in_bps(pnl, signal)
    b_size = book_size(signal)
    return sharpe, turnover, bias, b_size

def compute_dfs(prices: pd.DataFrame, composition: pd.DataFrame, t1=5, t2=0, mp=0):
    ret = prices / prices.shift() - 1
    presence = composition.reindex_like(ret).fillna(False)
    # voir les détails de pour
    historical_ret = ret.rolling(t1-t2, min_periods=mp).mean().shift(t2)[presence]
    return ret, presence, historical_ret

def plot_pnl_cumsum(pnl: pd.Series, title='', figsize=(15, 5), savedir=None, savename=None):
    plt.figure(figsize=figsize)
    plt.title(title)
    pnl.cumsum().plot()
    plt.grid(True)
    if savedir is not None:
        if not os.path.isdir(savedir):
            os.makedirs(savedir)
        plt.savefig(f"{savedir}/{savename}")


def config_hash(universe: str, strategy: str, t1: int, t2: int, mp: int, lsr: float=None):
    to_insert = f'{lsr}' if 'EW' in strategy else ''
    return f"{universe}_{strategy}{to_insert}_1t{t1}_2t{t2}_mp{mp}".replace('.', '')


def compute_index_perf(mkt_cap: pd.DataFrame, composition: pd.DataFrame, prices: pd.DataFrame):
    presence_mkt = composition.reindex_like(mkt_cap).fillna(False)
    norm_mkt_cap = cross_section_normalization(mkt_cap[presence_mkt])
    index_level = (norm_mkt_cap * prices).sum(axis=1).replace(0, np.nan).dropna()
    index_ret = index_level / index_level.shift() - 1
    return index_level, index_ret
    


