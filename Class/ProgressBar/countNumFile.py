import os


def count_files(folder):
    num_files = 0
    for root, dirs, files in os.walk(folder):
        num_files += len(files)
    return num_files
