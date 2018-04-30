import os
import pandas as pd

data = pd.DataFrame()
directory = os.getcwd()

visited = 0

for filename in sorted(os.listdir(directory)):
	if filename.endswith('.csv'):
		new_data = pd.read_csv(filename)

		if visited == 0:
			data = new_data
		else:
			data = data.merge(new_data, on='subreddit')
			print(visited)

		visited += 1

data.to_csv('features.csv', index=False)


# data.to_csv('features.csv', mode='w', index=False)