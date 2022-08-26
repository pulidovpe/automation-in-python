# test-os-module.py

import os
import glob
import time
from pathlib import Path

name_dir = 'test_dir'

# Show the path
main_path = os.getcwd()

print(f'Creating {name_dir} directory...')
if os.path.exists(name_dir) == False:
    # Create a folder
    os.mkdir(name_dir)
else:
    print(f'{name_dir} already exist!')

# Change to the new directory
os.chdir(name_dir)

# Get and show the new path
new_path = os.getcwd()
print(f'Current directory {new_path}')

time.sleep(1)

# Create some files in loop
for x in range(1,11):
    ##os.mknod(f'test{x}.txt')
    testfile = open(f'test{x}.txt', 'w')
    testfile.write(f'Name: test{x}.txt')
    print(f'test{x}.txt')
testfile.close()

# Show the files
os.listdir()

time.sleep(1)

# To join two paths together
path_joined = os.path.join(new_path, "**/*.txt")

# Get a recursive list of file paths that matches pattern including sub directories
fileList = glob.glob(path_joined, recursive=True)

# Iterate over the list of filepaths & remove each file.
print(f'Removing files in {new_path}')
for filePath in fileList:
    try:
        os.remove(filePath)
    except OSError:
        print(f'Error while deleting file {filePath}')

# Get out of the directory
os.chdir("..")

# Remove directory
print(f'Removing directory {name_dir}')
os.rmdir(name_dir)
