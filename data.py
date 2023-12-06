import pandas as pd


def update_data():
    df = pd.read_csv('fragments.csv')

    killsPerDay = df.groupby('Date')['Kills'].sum()
    print(killsPerDay)
    fraggiesPerDay = df.groupby('Date')['Farmed'].sum()
    maxFrag = df.groupby('Date')['Farmed'].max()
    minFrag = df.groupby('Date')['Farmed'].min()
    avgFraggies = df.groupby('Date')['Farmed'].mean()
    perThousand = killsPerDay / fraggiesPerDay

    result_df = pd.concat([killsPerDay, fraggiesPerDay, maxFrag, minFrag, avgFraggies, perThousand], axis=1)
    result_df.columns = ['Kills', 'Total Fraggies', 'High Roll', 'Low Roll', 'Average', 'KP Fraggies']
    result_df.to_csv('data.csv')
    print(result_df)
    print('--------------------------------------------------------------------------------')


if __name__ == '__main__':
    update_data()
