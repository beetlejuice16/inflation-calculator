import pandas as pd
import numpy as np 

class Inflation:

    def __init__(self, ref, tar, amount, csv_file='Germany_PI_1991-2020'):
        
        self.data = pd.read_csv(csv_file, index_col=0)
        self.ref_index = self.data['Consumer price index'][ref]
        self.tar_index = self.data['Consumer price index'][tar]
        self.amount = amount
    
    def get_ratio(self):

        ratio = self.tar_index / self.ref_index

        return ratio

    def convert(self):

        ratio = self.get_ratio()
        final_amount = ratio * self.amount

        return final_amount

def run():
    ref = int(input("Enter starting year: "))
    tar = int(input("Enter target year: "))
    amount = float(input("Enter amount to be converted: "))

    inflation = Inflation(ref, tar, amount)

    final_amount = round(inflation.convert(), 2)

    return ref, tar, amount, final_amount


def main():
    ref, tar, amount, final_amount = run()
    print(f'{amount} in {ref} is worth {final_amount} in {tar}.')

if __name__ = "__main__":
    main()
