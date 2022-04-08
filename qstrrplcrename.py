#!/usr/bin/env python3
import sys, os


def stringReplaceRename(src, dst):
    for filename in os.listdir():
        os.rename(filename, filename.replace(src, dst))
        # print(filename)
    return


if __name__ == "__main__":
    if len(sys.argv) > 1:
        src = sys.argv[1]
        if len(sys.argv) == 2:
            dst = ""
        else:
            dst = sys.argv[2]
        stringReplaceRename(src, dst)
    else:
        print("pass src and dst as args")
