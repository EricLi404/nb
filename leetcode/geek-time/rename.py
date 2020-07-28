import os
import sys

from glob2 import glob


def rename(d):
    f = glob(d + "/*")
    for i in f:
        if "[" in i and "]" in i:
            nm = i.replace("[", "")
            nm = nm.replace("]", "_")
            os.rename(i, nm)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        exit(-1)
    d = sys.argv[1]
    rename(d)
