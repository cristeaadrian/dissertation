# Import library and dataset
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_style('darkgrid')
sns.set(rc={'figure.figsize':(20,7)})

subreddit_counts = pd.read_csv('counts.csv')

counts = subreddit_counts['count_reddit'][:30][::-1]
names = subreddit_counts['subreddit'][:30][::-1]

plt.subplot(1, 2, 1)
y_pos = np.arange(len(names))
plt.barh(y_pos, counts)
plt.yticks(y_pos, names)
plt.xlabel('Subreddit Comment Count')
plt.title("Top 30 subreddits by number of comments")

plt.subplot(1, 2, 2)
c = 0.0000000001
plt.title("Power Law Distribution")
plt.xlabel('Log(Rank of Subreddits)')
plt.ylabel('Log(Subreddit Comment Count)')
plt.plot(np.log(range(1,13001)),
         subreddit_counts['count_reddit'].apply(lambda x: np.log(c + x)))

# Show graphic
plt.tight_layout()
plt.show()