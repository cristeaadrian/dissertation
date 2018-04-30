import csv
import os
import sys
import operator
import pandas as pd
from collections import defaultdict


def main(argv):
    w2i = defaultdict(int)
    i2w = defaultdict(str)
    visit_count = defaultdict(int)
    num_subreddit = int(argv)
    reddit_count = pd.read_csv('counts0517.csv')
    reddit_name = reddit_count.subreddit
    name_list = list(reddit_name[:num_subreddit])
    for index, content in enumerate(name_list):
        w2i[content] = index
        i2w[index] = content
    author_reddit = defaultdict(list)
    for i in range(5):
        file_name = '00000000000' + str(i)
        with open(file_name, 'r') as in_file:
            for line in in_file:
                author, subreddit = line.strip().split(',')
                if subreddit in w2i.keys():
                    if author not in author_reddit.keys():
                        author_reddit[author] = [w2i[subreddit]]
                    elif w2i[subreddit] not in author_reddit[author]:
                        author_reddit[author].append(w2i[subreddit])

        print(len(author_reddit.keys()))
        in_file.close()

    new_file_name = 'new_file_nodup_' + str(num_subreddit) + '.csv'
    with open(new_file_name, 'w') as out_file:
        headers = ['from', 'to', 'weight']
        f_csv = csv.writer(out_file)
        f_csv.writerow(headers)

        for author in author_reddit.keys():

            reddits_connected = author_reddit[author]
            for j in range(len(reddits_connected)):
                for k in range(j, len(reddits_connected)):
                    source = reddits_connected[j]
                    target = reddits_connected[k]
                    row = sorted([source, target])
                    row = [str(row[0]), str(row[1])]
                    row = ','.join(row)
                    if source != target:
                        if row not in visit_count.keys():
                            visit_count[row] = 1
                        else:
                            visit_count[row] += 1

        sorted_visit = sorted(visit_count.items(), key=operator.itemgetter(1))
        for i in range(len(sorted_visit)):
            if i < 0.1 * len(sorted_visit):
                del sorted_visit[i]

        visit_count = dict(sorted_visit)

        for row in visit_count.keys():
            source, target = row.strip().split(',')
            if visit_count[row] > 1:
                row_data = [int(source), int(target), visit_count[row]]
                f_csv.writerow(row_data)
    out_file.close()


if __name__ == "__main__":
    main(sys.argv[1])
