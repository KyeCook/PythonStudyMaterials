#####
#
#
# Python shell utilities
#
#####

import os
import shutil

from os import path
from shutil import make_archive
from zipfile import ZipFile

def main():
    # Create a duplicate of existing file
    if path.exists("textfile.txt"):
        # get path to file
        src = path.realpath("textfile.txt")

        # seperate path from file name
        head, tail = path.split(src)
        print("Path = " + head)
        print("File name = " + tail)

        # Create backup of file by appending "bak" to file
        dst = src + ".bak"

        # Use shell utility to copy the file
        shutil.copy(src, dst)

        # Use shell utility to copy the file with : permissions, modifcation times etc. (metadata)
        shutil.copystat(src,dst)

        # rename original file
        os.rename("textfile.txt", "newfile.txt")

        # Put files into zip archive
        root_dir, tail = path.split(src)
        shutil.make_archive("archive", "zip", root_dir)

        # More specific control over zipfiles

        with ZipFile("test.zip", "w") as newzip:
            newzip.write("textfile.txt")
            newzip.write("textfile.txt.bak")


if __name__ == '__main__':
    main()
