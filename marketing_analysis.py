import pandas as pd

def load_data():
    return pd.read_csv('data/engineered_data.csv')

def summarize(df):
    print("Customer Summary:")
    print(df[['Age', 'Income', 'Total_Spending', 'Total_Purchases']].describe())

if __name__ == '__main__':
    df = load_data()
    summarize(df)
