# imports
import numpy as np
from scipy.stats import norm

# distance current price is from strike price
def d1(S, K, sigma, T = (1/365), r = 0):
    d1_value = (np.log(S / K) + (r + ((sigma)**2) / (2)) * T) / (sigma * np.sqrt(T))
    return d1_value


# probability adjusted distance to strike price
def d2(S, K, sigma, T = (1/365), r = 0):
    d2_value = d1(S, K, sigma, T, r) - (sigma * np.sqrt(T))
    return d2_value


# theoretical worth of over bet 
def call(S, K, sigma, T, r):
    call_value = (S * norm.cdf(d1(S, K, sigma, T, r))) - (K * np.exp(-r * (T)) * norm.cdf(d2(S, K, sigma, T, r)))
    return float(round(call_value, 3))


# theoretical worth of under bet
def put(S, K, sigma, T, r):
    put_value = (K * np.exp(-r * T) * norm.cdf(-(d2(S, K, sigma, T, r)))) - (S * norm.cdf(-d1(S, K, sigma, T, r)))
    return float(round(put_value, 3))


def black_scholes(S, K, sigma, T, r):
    return (call(S, K, sigma, T, r), put(S, K, sigma, T, r))

# test run
# print(black_scholes(27.3, 25.5, 0.18, 1/365, 0))