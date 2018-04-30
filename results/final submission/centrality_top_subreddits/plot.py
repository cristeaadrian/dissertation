# Import library and dataset
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_style('darkgrid')
sns.set(rc={'figure.figsize':(10,17)})

centrality = pd.read_csv('centrality.csv', index_col=0)
centrality['subreddit'] = centrality['subreddit'].astype(str).str[:-4]
counts = pd.read_csv('counts.csv')

merged = pd.merge(centrality, counts,
                  left_index=False,
                  right_index=False,
                  on='subreddit',
                  sort=False)

betweenness = merged.sort_values(by=['betweenness'],
                                 ascending=False)[['subreddit', 'betweenness', 'count_reddit']]

degree = merged.sort_values(by=['degree'],
                                 ascending=False)[['subreddit', 'degree', 'count_reddit']]

closeness = merged.sort_values(by=['closeness'],
                                 ascending=False)[['subreddit', 'closeness', 'count_reddit']]

eigen_centrality = merged.sort_values(by=['eigen_centrality'],
                                      ascending=False)[['subreddit', 'eigen_centrality', 'count_reddit']]

# BETWEENNESS
plt.subplot(211)
sns.regplot(x=betweenness['count_reddit'], y=betweenness['betweenness'], fit_reg=False)
plt.title("(a) Relation number of comments and betweenness")
plt.xlabel('Total Comments')
plt.yticks(rotation=45)
plt.ylabel('Betweenness Score')

plt.subplot(212)
num = 5000
height = betweenness['betweenness'][:num]
bars = betweenness['subreddit'][:num]
plt.plot(range(num), height.apply(lambda x: np.log(x)))
plt.xticks(rotation=45)
plt.locator_params(nbins=40, axis='x')
plt.title("(b) Distribution of betweenness scores of subreddits")
plt.ylabel('Betweenness Score (Log scale)')
plt.xlabel('Rank of subreddit (by number of comments)')
plt.margins(0)
#plt.tight_layout()
#plt.show()
plt.draw()
plt.savefig('betweenness.png')
plt.clf()

# degree
plt.subplot(211)
sns.regplot(x=degree['count_reddit'], y=degree['degree'], fit_reg=False)
plt.title("(a) Relation number of comments and degree")
plt.xlabel('Total Comments')
plt.yticks(rotation=45)
plt.ylabel('Degree Score')

plt.subplot(212)
num = 5000
height = degree['degree'][:num]
bars = degree['subreddit'][:num]
plt.plot(range(num), height.apply(lambda x: np.log(x)))
plt.xticks(rotation=45)
plt.locator_params(nbins=40, axis='x')
plt.title("(b) Distribution of degree scores of subreddits")
plt.ylabel('Degree Score (Log scale)')
plt.xlabel('Rank of subreddit (by number of comments)')
plt.margins(0)
#plt.tight_layout()
#plt.show()
plt.draw()
plt.savefig('degree.png')
plt.clf()

# closeness
plt.subplot(211)
sns.regplot(x=closeness['count_reddit'], y=closeness['closeness'], fit_reg=False)
plt.title("(a) Relation number of comments and closeness")
plt.xlabel('Total Comments')
plt.yticks(rotation=45)
plt.ylabel('Closeness Score')

plt.subplot(212)
num = 5000
height = closeness['closeness'][:num]
bars = closeness['subreddit'][:num]
plt.plot(range(num), height.apply(lambda x: np.log(x)))
plt.xticks(rotation=45)
plt.locator_params(nbins=40, axis='x')
plt.title("(b) Distribution of closeness scores of subreddits")
plt.ylabel('Closeness Score (Log scale)')
plt.xlabel('Rank of subreddit (by number of comments)')
plt.margins(0)
#plt.tight_layout()
#plt.show()
plt.draw()
plt.savefig('closeness.png')
plt.clf()

# eigen_centrality
plt.subplot(211)
sns.regplot(x=eigen_centrality['count_reddit'], y=eigen_centrality['eigen_centrality'], fit_reg=False)
plt.title("(a) Relation number of comments and eigenvector centrality")
plt.xlabel('Total Comments')
plt.yticks(rotation=45)
plt.ylabel('Eigenvector Centrality Score')

plt.subplot(212)
num = 5000
height = eigen_centrality['eigen_centrality'][:num]
bars = eigen_centrality['subreddit'][:num]
plt.plot(range(num), height.apply(lambda x: np.log(x)))
plt.xticks(rotation=45)
plt.locator_params(nbins=40, axis='x')
plt.title("(b) Distribution of eigenvector centrality scores of subreddits")
plt.ylabel('Eigenvector Centrality Score (Log scale)')
plt.xlabel('Rank of subreddit (by number of comments)')
plt.margins(0)
#plt.tight_layout()
#plt.show()
plt.draw()
plt.savefig('eigen_centrality.png')
plt.clf()