import os

def file_count():
    # local variable
    files = os.listdir(os.getcwd())

    count = 0
    for item in files:
        if os.path.isfile(item):
            count += 1

    print("Number of files in the present working directory:", count)


# function call
file_count()

