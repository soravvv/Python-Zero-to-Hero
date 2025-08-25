import os;

for i in range(0, 3):
    os.rename(f"example-folders/example-folder-{i+1}", f"example-folders/renamed-{i+1}")