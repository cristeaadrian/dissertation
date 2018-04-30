import os
import pandas as pd
from pathlib import Path

p = Path(__file__).parents[2]
os.chdir(str(p) + '/data/1217/subreddit_comment_pair/top1000')

data = pd.read_csv('1217_liwc_results.txt', sep='\t')
data.to_csv('1217_liwc_results.csv')