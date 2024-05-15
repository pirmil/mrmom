import pandas as pd
import numpy as np

prices_list = np.array([
    [100.25, 105.50, 98.75, 102.30, 99.80, 101.75, 104.20, 97.90, 103.40, 106.60],
    [75.60, 78.90, 76.30, 79.10, 80.20, 77.50, 82.10, 81.30, 83.20, 85.10],
    [55.80, 58.20, 57.10, 56.40, 59.30, 61.20, 60.70, 62.80, 63.50, 65.00]
])
prices = pd.DataFrame(prices_list.T, columns=['stock_a', 'stock_b', 'stock_c'], index=['t0', 't1', 't2', 't3', 't5', 't8', 't9', 't11', 't12', 't13'])



composition_list = np.array([
    [True, False, True, False, True, False, True, True, True, False],
    [False, True, True, True, False, True, True, True, False, True],
    [True, False, True, True, True, True, True, False, True, False]
])
composition = pd.DataFrame(composition_list.T, columns=['stock_a', 'stock_b', 'stock_c'], index=['t0', 't1', 't2', 't3', 't4', 't6', 't7', 't8', 't9', 't11'])

mkt_cap_list = np.array([
    [10.5, 12.8, 15.2, 9.7, 11.3, 13.6, 16.1, 8.4, 10.9, 14.7],
    [25.6, 22.1, 27.9, 24.3, 20.8, 26.4, 23.7, 19.5, 28.2, 21.0],
    [7.2, 5.9, 8.6, 6.3, 9.1, 4.8, 7.5, 10.2, 5.4, 8.9]
])
mkt_cap = pd.DataFrame(mkt_cap_list.T, columns=['stock_a', 'stock_b', 'stock_c'], index=['t-1', 't0', 't1', 't3', 't6', 't8', 't9', 't11', 't13', 't15'])