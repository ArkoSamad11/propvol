# imports required functions for calculations of greeks
from src.pricer.black_scholes import d1, d2

# S represents rolling average for stat
# theoretical change in over bet value when S moves by 1
def call_delta(S, K, sigma, T = 1/365, r = 0):
    pass
# theoretical change in under bet value when S moves by 1
def put_delta(S, K, sigma, T = 1/365, r = 0):
    pass
# theoretical change in delta when S moves by 1
def gamma(S, K, sigma, T = 1/365, r = 0):
    pass
# theoretical change in O/U value when volatility changes by .01
def vega(S, K, sigma, T = 1/365, r = 0):
    pass
# theoretical price change per day --> slightly irrelevant because T = 1/365 for practically all bets
def call_theta(S, K, sigma, T = 1/365, r = 0):
    pass
def put_theta(S, K, sigma, T = 1/365, r = 0):
    pass
# theoretical price change with risk free rate --> time to maturity is negligible, 48 minute games 
def call_rho(S, K, sigma, T = 1/365, r=0):
    pass
def put_rho(S, K, sigma, T = 1/365, r=0):
    pass
