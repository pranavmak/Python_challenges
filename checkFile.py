import os.path 

file_path = '\SRE_DevOps_Skills\Python\Coding_Practice\example.txt'

if os.path.exists(file_path):
    print("File exists.")
else:
    print(f"'{file_path}' does not exist.")