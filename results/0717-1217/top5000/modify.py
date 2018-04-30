import pandas as pd

data = pd.read_csv('features.csv')
data.drop('Unnamed: 0', axis=1, inplace=True)
new_data = pd.read_csv('avg_authors_and_posts.csv')

data['AvgAuthor'] = new_data['AvgAuthor']
data['AvgPost'] = new_data['AvgPost']

data.to_csv('features.csv', mode='w', index=False)