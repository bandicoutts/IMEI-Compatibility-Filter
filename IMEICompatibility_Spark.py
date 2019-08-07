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
    new_dict[row[0]] = row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]

for key,value in new_dict.items():
  if key not in old_dict:
    try:
      filtered_dict[key] = value[0], value[1], value[2], value[3], value[4], value[5], value[6], value[7], value[8]
    except:
      filtered_dict[key] = value[0], value[1], value[2], value[3], value[4], value[5], value[6], value[7], "FALSE"

with open(output_file, 'w') as f: 
    f.write("%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n"%("tac_code","model_family","w850_flag","w2100_flag", "lte700_flag", "lte1800_flag", "lte2600_flag", "lte2300_flag","utms_3g_capable","utms_4g_capable"))
    for key, value in filtered_dict.items():
        f.write("%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n"%(key,value[0], value[1], value[2], value[3], value[4], value[5], value[6], value[7], value[8]))
