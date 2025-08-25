import os;
folders = os.listdir("example-folders")

print(folders)

for folder in folders:
    print(folder) # for printing folder

for folder in folders:
    print(os.listdir(f"example-folders/{folder}")) # this will each file name inside the folder

print(os.getcwd()) # get current working directory

os.chdir("/Personal Learning") # change working directory
print(os.getcwd())