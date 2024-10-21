import os
from traceback import print_exc


def print_docs (directory):
    all_files = os.walk(directory)
    for catalog in all_files:
        print('Папка {catalog[8]} содержит:')
        print (f' Директории: {", ".join([folder for folder in catalog[1]])}')
        print (f'Файлы: {", ".join([file for file in catalog[2]])}')
        print('-' * 40)

print_docs("/Users/46acf/eclipse")
