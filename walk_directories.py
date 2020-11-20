import os

walk_path = r'c:\py3master'


for dirpath, dirnames, filenames in os.walk(walk_path):
    for filename in filenames:
        if ".py" in filename:
            print(f'{filename} - ({dirpath})')
