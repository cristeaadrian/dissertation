import os
import csv
import argparse
import pandas as pd
from pathlib import Path
from collections import defaultdict

parser = argparse.ArgumentParser(description="Read CSV files from the specified folder (inside the data folder)")
parser.add_argument('--date',
                    type=str,
                    nargs='?',
                    default='1217',
                    action='store',
                    help='choose the date to analyse (eg. 0517 or 1217')
parser.add_argument('--sub_num',
                    type=str,
                    nargs='?',
                    default='1000',
                    action='store',
                    help='choose the number of top subreddits (by number of comments) to take into account (eg. 1000 or 15000')
args = parser.parse_args()

date = str(args.date)
sub_num = str(args.sub_num)
p = Path(__file__).parents[2]
os.chdir(str(p) + '/data/' + date + '/counts')

w2i = defaultdict(int)
i2w = defaultdict(str)
NUM_SUBREDDIT = int(sub_num)
reddit_count = pd.read_csv(date + '_counts_' + sub_num + '.csv')
reddit_name = reddit_count.subreddit
name_list = list(reddit_name[:NUM_SUBREDDIT])
for index, content in enumerate(name_list):
    w2i[content] = index
    i2w[index] = content

os.chdir(str(p) + '/results/' + date + '/top' + sub_num)

with open('new_file_nodes_' + sub_num + '.csv', 'w') as out_file:
    headers = ['ID', 'name']
    f_csv = csv.writer(out_file)
    f_csv.writerow(headers)
    for key in i2w.keys():
        row = [key, i2w[key]]
        f_csv.writerow(row)