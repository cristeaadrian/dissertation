import pandas as pd

data = pd.read_csv('centrality.csv', index_col=0)

data['subreddit'] = data['subreddit'] + '.txt'
data.to_csv('centrality.csv')