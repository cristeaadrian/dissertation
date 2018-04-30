import pandas as pd

centrality = ['betweenness','closeness','eigen_centrality','degree']
to_merge = ['{}_centrality.csv'.format(i) for i in centrality]
dfs = []
count = 0
df = pd.read_csv(to_merge[0], header=0)
df = df.ix[:,0]
dfs.append(df)
for filename in to_merge:
    # read the csv, making sure the first two columns are str
    df = pd.read_csv(filename, header=0)
    # throw away all but the first two columns
    df = df.ix[:,1]
    # change the column names so they won't collide during concatenation
    # df.columns = [filename + str(cname) for cname in df.columns]
    dfs.append(df)
# concatenate them horizontally
merged = pd.concat(dfs,axis=1)
# merged.columns = centrality

# write it out
merged.to_csv("merged.csv")
