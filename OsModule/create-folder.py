import os

if(not os.path.exists("example-folders")):
    os.mkdir("example-folders")

for i in range(0, 3):
    os.mkdir(f"example-folders/example-folder-{i+1}")