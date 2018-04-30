"""
Simple script used to download the previous years masters data
Can be adapted to different months data easily (I hope)
"""

from urllib.request import urlretrieve

file_names = []

for i in range(50):
    file_names.append(str(i).zfill(12))

print("Requesting the following files: ")
print(file_names)

for file_name in file_names:
    urlretrieve("https://storage.googleapis.com/fyp_reddit/0517/" + file_name, file_name)
    print("Downloaded file " + file_name)
