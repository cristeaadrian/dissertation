import os
import sys
import json
import argparse
from pathlib import Path

parser = argparse.ArgumentParser(description="Read CSV files from the specified folder (inside the data folder)")
parser.add_argument('--date',
                    type=str,
                    nargs='?',
                    default='0717-1217',
                    action='store',
                    help='choose the date to analyse (eg. 0517 or 1217')
parser.add_argument('--sub_num',
                    type=str,
                    nargs='?',
                    default='13000',
                    action='store',
                    help='choose the number of top subreddits (by number of comments) to take into account (eg. 1000 or 15000')
args = parser.parse_args()

date = str(args.date)
if args.sub_num == 'all':
    sub_num = 'all'
else:
    sub_num = 'top' + str(args.sub_num)

wk_dir = os.path.dirname(os.path.realpath('__file__'))

p = Path(wk_dir).parents[2]
os.chdir(str(p) + '/data/' + date + '/subreddit_comment_pair/' + sub_num)
num_files = len(os.listdir(os.getcwd()))

num_comments = dict()

for i in range(num_files):
    in_file = str(i).zfill(12)
    print("Processing file: {}".format(in_file))
    with open(in_file, 'r') as file:
        for line in file:
            subreddits = json.loads(line)
            subreddit = subreddits['subreddit']
            if subreddit not in num_comments:
                num_comments[subreddit] = 0
            elif num_comments[subreddit] <= 3:
                num_comments[subreddit] += 1
                body = subreddits['body']
                out_name = subreddit + '.txt'
                with open(out_name, 'a+') as out:
                    out.write(body)
