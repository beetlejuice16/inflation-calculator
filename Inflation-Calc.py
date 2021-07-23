import pandas as pd
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt

class Inflation:

    def __init__(self, csv_file, ref, tar):
        
        self.data = pd.read_csv(csv_file, index_col=0)
        self.ref = self.data['Consumer price index'][ref]
        self.tar = self.data['Consumer price index'][tar]