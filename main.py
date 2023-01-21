from Pricing.price_simulator import SimulatePrices
import pandas as pd
import numpy as np
import os

def read_data(data):
    return pd.read_csv(data)


if __name__ == "__main__":
    data_location = r"greeks.csv"
    data = read_data(data_location)
    instance = SimulatePrices(M=100, S0=100, n=252, T=3, sigma=0.2, mu=0.1)
    gbm_prices = SimulatePrices.gbm(instance)
    abm_prices = SimulatePrices.abm(instance)
    print("123")