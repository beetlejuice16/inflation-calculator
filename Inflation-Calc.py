import pandas as pd


class Inflation:

    def __init__(self, ref: int, tar: int, amount: float,
                 csv_file='Germany_PI_1991-2020'):

        self.data = pd.read_csv(csv_file, index_col=0)
        self.ref_index = self.data['Consumer price index'][ref]
        self.tar_index = self.data['Consumer price index'][tar]
        self.amount = amount

    def get_ratio(self) -> float:
        return self.tar_index / self.ref_index

    def convert(self) -> float:
        return self.amount * self.get_ratio()

def main():
    ref = int(input("Enter starting year: "))
    tar = int(input("Enter target year: "))
    amount = float(input("Enter amount to be converted: "))

    inflation = Inflation(ref, tar, amount)
    final_amount = round(inflation.convert(), 2)
    
    print(f'{amount} in {ref} is worth {final_amount} in {tar}.')


if __name__ == "__main__":
    main()
