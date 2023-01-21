import pandas as pd
import numpy as np

class DeltaGammaVega():
    def __init__(self, greeks, sims):
        self.greeks = greeks
        self.sims = sims

    def calc_dgv(self):
        return None