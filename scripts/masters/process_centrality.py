import csv
import sys
import re
import collections


def main(argv):
    centrality = collections.defaultdict(str)
    name_list = []
    value_list = []
    entry_list = []
    counts = 0
    open_file = argv + '.txt'
    with open(open_file, 'r') as in_file:
        matches = re.compile(r'\S+')
        for line in in_file:
            counts += 1
            for entry in matches.finditer(line):
                entry_list.append(entry.group())
            if counts % 2 != 0:
                name_list = entry_list
                entry_list = []
            else:
                value_list = entry_list
                entry_list = []
                for name, value in zip(name_list, value_list):
                    centrality[name] = value

                name_list = []
                value_list = []
    out_name = argv + '_centrality.csv'
    with open(out_name, 'w') as out_file:
        headers = ['subreddit', argv]
        f_csv = csv.writer(out_file)
        f_csv.writerow(headers)
        od_centrality = collections.OrderedDict(sorted(centrality.items()))
        for name in od_centrality.keys():
            f_csv.writerow([name, centrality[name]])

        # print(entry.group())


# if __name__ == '__main__':
# 	main(sys.argv[1])
centrality = ['betweenness', 'closeness', 'eigen_centrality', 'degree']
for i in centrality:
    main(i)
