from src.pricer.black_scholes import black_scholes
from src.pricer.greeks import vega
from src.analysis.realized_vol import realized_vol

def newton_raphson(market_price, S, K, sigma, T = 1/365, r = 0, max_iterations = 100):
    count = 0
    black_scholes_value = black_scholes(S, K, sigma, T, r)
    while abs(black_scholes_value - market_price) > 1e-6 and count < max_iterations:
        error = black_scholes_value - market_price
        vega_value = vega(S, K, sigma, T, r)
        if vega_value < 1e-8:
            raise ValueError('Vega is too low')
        adjusted_sigma = error / vega_value
        sigma = sigma - adjusted_sigma
        if sigma < 0:
            sigma = 1e-4
        count += 1
        black_scholes_value = black_scholes(S, K, sigma, T, r)
    if count == max_iterations:
        raise ValueError("Newton-Raphson did not converge")
    return sigma, count
    
