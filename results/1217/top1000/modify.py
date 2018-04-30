import pandas as pd

data = pd.read_csv('features.csv')

# data['X'] = pd.Series(range(1000))
#
# cols = data.columns.tolist()
# cols = [cols[2]] + [cols[-1]] + cols[0:2] + cols[3:len(cols)-1]
#
# data = data[cols]
#
# data.to_csv('features.csv')
