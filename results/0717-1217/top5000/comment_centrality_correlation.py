import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.api as sm
import seaborn as sns

centrality = pd.read_csv('centrality.csv', index_col=0)
counts = pd.read_csv('counts.csv')

# print(centrality.head())
# print(counts.head())

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

# x = betweenness['betweenness']
# y = betweenness['count_reddit']
# model = sm.OLS(x, y).fit()
# with open("betweenness_regression.txt", "w") as text_file:
#     text_file.write(str(model.summary().as_text()))
#
# x = degree['degree']
# y = degree['count_reddit']
# model = sm.OLS(x, y).fit()
# with open("degree_regression.txt", "w") as text_file:
#     text_file.write(str(model.summary().as_text()))
#
# x = closeness['closeness']
# y = closeness['count_reddit']
# model = sm.OLS(x, y).fit()
# with open("closeness_regression.txt", "w") as text_file:
#     text_file.write(str(model.summary().as_text()))
#
# x = eigen_centrality['eigen_centrality']
# y = eigen_centrality['count_reddit']
# model = sm.OLS(x, y).fit()
# with open("eigen_centrality_regression.txt", "w") as text_file:
#     text_file.write(str(model.summary().as_text()))

# betweenness[:10].to_csv(path_or_buf='betweenness_top10.csv', index=False)
# degree[:10].to_csv(path_or_buf='degree_top10.csv', index=False)
# closeness[:10].to_csv(path_or_buf='closeness_top10.csv', index=False)
# eigen_centrality[:10].to_csv(path_or_buf='eigen_centrality_top10.csv', index=False)