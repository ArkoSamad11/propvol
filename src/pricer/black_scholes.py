# imports
import math as math
from scipy.stats import norm

# distance current price is from strike price
def d1(S, K, sigma, T = (1/365), r = 0):
    d1_value = (math.log(S / K) + (r + ((sigma)**2) / (2)) * T) / (sigma * math.sqrt(T))
    return d1_value
# probability adjusted distance to strike price
def d2(S, K, sigma, T = (1/365), r = 0):
    d2_value = d1(S, K, sigma, T, r) - (sigma * math.sqrt(T))
    return d2_value
# theoretical worth of over bet 
def call(S, K, sigma, T, r):
    call_value = (S * norm.cdf(d1(S, K, sigma, T, r))) - (K * math.exp(-r * (T)) * norm.cdf(d2(S, K, sigma, T, r)))
    return float(round(call_value, 2))
# theoretical worth of under bet
def put(S, K, sigma, T, r):
    put_value = (K * math.exp(-r * T) * norm.cdf(-(d2(S, K, sigma, T, r)))) - (S * norm.cdf(-d1(S, K, sigma, T, r)))
    return float(round(put_value, 2))
def black_scholes(S, K, sigma, T, r):
    return (call(S, K, sigma, T, r), put(S, K, sigma, T, r))


