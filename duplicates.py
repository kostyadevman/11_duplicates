import os
import sys


def get_files_dict(folder):
    files_dict = {}
    for dir_path, dir_name, file_names in os.walk(folder):
        for file_name in file_names:
            file_path = os.path.join(dir_path, file_name)
            file_info = os.stat(file_path)
            file_size = file_info.st_size
            files_dict.setdefault((file_name, file_size), []).append(file_path)
    return files_dict


def print_duplicates(files_dict):
    for (file_name, file_size), paths in files_dict.items():
        if len(paths) > 1:
            print('Duplicates for file {}:'.format(file_name))
            print('\n'.join(paths))
            


if __name__ == '__main__':
    if not sys.argv[1:] or not os.path.isdir(sys.argv[1]):
        exit('Usage: python duplicates.py <path to dir>')

    src_dirname = sys.argv[1]

    files_dict = get_files_dict(src_dirname)
    print('Found duplicates in a directory {}:'.format(src_dirname))
    print_duplicates(files_dict)