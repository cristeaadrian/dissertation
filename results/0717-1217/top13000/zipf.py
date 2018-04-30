# Import library and dataset
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_style('darkgrid')

subreddit_counts = pd.read_csv('counts.csv')

c = 0.0000000001

plt.xlabel('Log(rank of subreddits)')
plt.ylabel('Log(subreddit comment numbers)')

plt.plot(np.log(range(1,13001)),
         subreddit_counts['count_reddit'].apply(lambda x: np.log(c + x)))
plt.show()