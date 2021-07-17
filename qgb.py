#!/usr/bin/env python3
import sys
import os

args = sys.argv
if len(args) > 1:
    if args[1] == "f":
        commandprefix = "GO111MODULE=off "
    else:
        commandprefix = ""

os.system(f"{commandprefix}go build")
