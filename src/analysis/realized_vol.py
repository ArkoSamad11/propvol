import numpy as np

# historical volatility formula
def find_sigma(stat_list):
    stat_list = np.array(stat_list)
    log_returns = np.log(stat_list[:-1] / stat_list[1:])
    sigma = np.std(log_returns) * np.sqrt(82)
    return sigma