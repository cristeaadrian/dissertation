import json
from collections import defaultdict
from pprint import pprint

count = 1
# subreddit = defaultdict(str)
# data = defaultdict(list)
for i in range(5,50):
    if i < 10:
        in_file = '00000000000{0}'.format(i)
    else:
        in_file = '0000000000{0}'.format(i)
    with open(in_file, 'r') as f:
        for line in f:
            subreddits = json.loads(line)
            subreddit = subreddits['subreddit']
            data = subreddits['data']
            out_name = subreddit + '.txt'
            with open(out_name, 'w') as out:
                for i in range(len(data)):
                    out.write(data[i]['body'])
