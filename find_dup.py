"""
I want to implement a python program to find and delete duplicated files in my
hard driver then save disk space
steps:
1. find and delete and print duplicated files in one path
2. implement recursion for the parent folder and sub-folders
3. add UI, more class
4. multiple platform, windows and linux
5. improve performance
"""
import hashlib
from pathlib import Path
import os

duplicated_files = {}
deleted_files = []
photo_path = '/Users/yubchen/Pictures'


def md5sum(filename, blocksize=65536):
    hash = hashlib.md5()
    with open(filename, "rb") as f:
        for block in iter(lambda: f.read(blocksize), b""):
            hash.update(block)
    return hash.hexdigest()


def build_dup_dict(dir_path, pattern='*.jpg'):
    def save(file):
        hash = md5sum(file)
        if hash not in duplicated_files.keys():
            duplicated_files[hash] = [file]
        else:
            duplicated_files[hash].append(file)

    p = Path(dir_path)
    for item in p.glob('**/' + pattern):
        save(str(item))


def delete_file(files):
    i = 0
    for file in files:
        print("Delete... " + file)
        os.remove(file)
        i += 1
    print("There are " + str(i) + "duplicated files.")


def main():
    def get_duplicate():
        return {k: v for k, v in duplicated_files.items() if len(v) > 1}

    build_dup_dict(photo_path)
    print("List duplicated files here:")
    print("Hash:\t\t\t\t\t\t\t\tFile Names")
    for hash, files in get_duplicate().items():
        print("{}: {}".format(hash, files))
        while len(files) > 1:
            deleted_files.append(files.pop())
    delete_file(deleted_files)


if __name__ == '__main__':
    main()
