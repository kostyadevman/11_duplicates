import os
import sys


def get_files_by_size(folder):
    files_by_size = {}
    for dir_path, dir_name, file_names in os.walk(folder):
        for file_name in file_names:
            file_path = os.path.join(dir_path, file_name)
            file_info = os.stat(file_path)
            file_size = file_info.st_size
            files_by_size.setdefault((file_name, file_size), []).append(file_path)
    return files_by_size


def get_duplicates(files_by_size):
    duplicates_in_dir = []
    for file_size, duplicates in files_by_size.items():
        if len(duplicates) > 1:
            duplicates_in_dir.extend(duplicates[1:])  # The first is original
    return duplicates_in_dir


def remove_duplicates(duplicates):
    for duplicate in duplicates:
        os.remove(duplicate)
    return duplicates


if __name__ == "__main__":
    if not sys.argv[1:] or not os.path.isdir(sys.argv[1]):
        exit('Usage: python duplicates.py <path to dir>')

    src_dirname = sys.argv[1]

    files_by_size = get_files_by_size(src_dirname)
    duplicates = get_duplicates(files_by_size)

    print('Found duplicates in a directory "{}":'.format(src_dirname))
    for duplicate in duplicates:
        print(duplicate)
    user_answer = input('Do You want to remove duplicates [Yes/No]: ')
    positive_answers = ['Yes', 'yes', 'YES', 'Y', 'y']
    if user_answer in positive_answers:
        remove_duplicates(duplicates)