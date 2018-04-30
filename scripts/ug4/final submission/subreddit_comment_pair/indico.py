import os, time
import indicoio
import numpy as np
import pandas as pd
from collections import OrderedDict


indicoio.config.api_key = 'd2907f54b0f01873808156222b16126c'


directory = 'converted_comments'
start_time = time.time()
added_header_to_csv = False
files_parsed = 0

output_dataframe = pd.read_csv('output.csv')
output_file = open("output.csv", "a")

for filename in sorted(os.listdir(directory)):
    visited = False
    if filename.endswith(".txt"):
        for subreddit in output_dataframe['subreddit']:
            if subreddit == filename:
                print("Skipping " + filename + "...")
                visited = True
                break

        if visited == False:
            for file in output_dataframe['subreddit'].str.contains(filename):
                if file == filename:
                    print("Yes!")
            print("Adding " + filename + "...")
            path = directory + '/' + filename
            with open(path, 'r') as myfile:
              data = myfile.read()



            response = indicoio.analyze_text(data, apis=['sentiment', 'emotion', 'personality', 'twitter_engagement'])

            # Build data dictionary
            d = OrderedDict()
            d['sentiment'] = response['sentiment']
            d.update(response['emotion'])
            d.update(response['personality'])
            # d.update(response['twitter_engagement'])
            d['twitter_engagement'] = response['twitter_engagement']

            # Convert to DataFrame
            columns = list(d.keys())
            values = list(d.values())
            arr_len = len(values)
            features = pd.DataFrame(np.array(values, dtype=object).reshape(1, arr_len), columns=columns, index=[filename])
            features.to_csv(output_file, mode='a', header=False)

        # # # Add to CSV
        # # if (not added_header_to_csv): # Add first row with header
        # #     features.to_csv(output_file)
        # #     added_header_to_csv = True
        # # else: # Append row to csv


output_file.close()
print("Time: ", time.time() - start_time)