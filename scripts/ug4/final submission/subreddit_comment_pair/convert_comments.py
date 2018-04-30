import pandas as pd

files = []
for i in range(4):
    in_file = str(i).zfill(12)
    files.append(in_file)

df = pd.DataFrame()
df = pd.concat((pd.read_csv(f) for f in files))

subreddits_dict = df.groupby('subreddit')
subreddits = list(subreddits_dict.groups.keys())

for subreddit in subreddits:
    with open(subreddit + '.txt', mode='a') as f:
        sub = subreddits_dict.get_group(subreddit)
        body = sub['body']
        body.to_csv(f, header=False, index=False)