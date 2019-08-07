import csv
import os

old_dict = {}
new_dict = {}
filtered_dict = {}
old_file = 'old_file.csv' # replace this with the directory and file name of the original file
new_file = 'new_file.csv' # replace this with the directory and file name of the new file
output_file = 'output_file.csv' # replace this with the directory and file name of the file you would like the results to be returned to

with open(old_file) as f:
  reader = csv.reader(f)
  for row in reader:
    old_dict[row[0]] = 1

with open(new_file) as m:
  reader = csv.reader(m)
  for row in reader:
    new_dict[row[0]] = row[1], row[2], row[3]

for key,value in new_dict.items():
  if key not in old_dict:
    filtered_dict[key] = value[0], (1 if value[1] == "TRUE" else 0), (1 if value[2] == "TRUE" else 0)

with open(output_file, 'w') as f: 
    f.write("%s,%s,%s,%s\n"%("TacCode","MktModel","DeviceBandW850","DeviceBandW2100"))
    for key, value in filtered_dict.items():
        f.write("%s,%s,%s,%s\n"%(key,value[0], value[1], value[2]))
