import csv
import pandas as pd
from collections import defaultdict

w2i = defaultdict(int)
i2w = defaultdict(str)
NUM_SUBREDDIT = 5000
reddit_count = pd.read_csv('counts.csv')
reddit_name = reddit_count.subreddit
name_list = list(reddit_name[:NUM_SUBREDDIT])
for index, content in enumerate(name_list):
    w2i[content] = index
    i2w[index] = content

# print(i2w[2000])
with open('nodes.csv','w') as out_file:
    headers = ['ID','name']
    f_csv = csv.writer(out_file)
    f_csv.writerow(headers)
    for key in i2w.keys():
        row = [key,i2w[key]]
        f_csv.writerow(row)

# with open('new_file_nodup.csv','r') as in_file, open('subreddit_link.csv','w') as out_file:
#     headers = ['source','target']
#     f_csv = csv.writer(out_file)
#     f_csv.writerow(headers)
#     for line in in_file:
#         source,target = line.strip().split(',')
#         if source != 'source':
#             source = int(source)
#             target = int(target)
#         # print(source.type())
#         # print(i2w[int(float(source))])
#         if source in i2w.keys():
#             row = [i2w[source],i2w[target]]
#             # print(row)
#             f_csv.writerow(row)
