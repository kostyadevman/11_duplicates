import os
import sys
import ntpath


def get_files_by_size(folder):
    files_by_size = {}
    for dirpath, dirname, files in os.walk(folder):
        for file in files:
            file_path = os.path.join(dirpath, file)
            file_info = os.stat(file_path)
            file_size = file_info.st_size
            files_by_size.setdefault(file_size, []).append(file_path)

    return files_by_size


def get_duplicates(files_by_size):
    unique = []
    duplicates = []
    for size in files_by_size:
        for file in files_by_size[size]:
            path, filename = ntpath.split(file)
            if filename not in unique:
                unique.append(filename)
            else:
                duplicates.append(file)
    return duplicates


def remove_duplicates(files):
    for file in files:
        os.remove(file)
    return files


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






