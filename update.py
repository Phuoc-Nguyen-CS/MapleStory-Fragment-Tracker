from data import update_data
import pandas as pd
import sys

df = pd.read_csv('fragments.csv')
result = pd.read_csv('data.csv')

if len(sys.argv) == 2 and sys.argv[1] == 'recent':
    print(df.tail())
    sys.exit(1)
elif len(sys.argv) == 2 and sys.argv[1] == 'total':
    print(result)
    sys.exit(1)
elif len(sys.argv) < 4:
    print(len(sys.argv))
    print("Usage: Kills, Start, End, Drop")
    sys.exit(1)

kills, sFrag, eFrag, drop = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

farmed = int(eFrag) - int(sFrag)
today = pd.to_datetime('today').normalize().date()

# Append Values
data = {'Kills': kills, 'Start': sFrag, 'End': eFrag, 'Farmed': str(farmed), 'Drop': drop, 'Date': today}
df2 = df.append(data, ignore_index=True)
df2.to_csv('fragments.csv', index=False)
print('--------------------------------------------------------------------------------')
print(df2)
print('--------------------------------------------------------------------------------')
update_data()