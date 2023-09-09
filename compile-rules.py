import yara
import sys
import os

# todo: validate cli arg == 1
n = len(sys.argv)

rule_path = sys.argv[1]

# check if  rule_path is a file or a dir

# if file:
# rules = yara.compile(rule_path)

# if dir:

rule_dict = {}

for subdir, dirs, files in os.walk(rule_path):
    for file in files:
        if file.endswith(".yara"):
            key = str(subdir.split('/')[-1] + "_" + file)
            print("Adding " + key + ", " + os.path.join(subdir, file) + " to rule dictionary.")
            
            rule_dict[key] = os.path.join(subdir, file)
            
compiled_rules = yara.compile(filepaths=rule_dict)
compiled_rules.save('rules.yara')
