#!/usr/bin/env python3
import sys
import os
from config import GOPRIVATE, PRIVATE_LIBRARIES

args = sys.argv
if len(args) > 1:
    os.system(
        f"GOPROXY=https://goproxy.io,direct GOPRIVATE={GOPRIVATE} go get {PRIVATE_LIBRARIES[args[1]]}"
    )
else:
    print("pass module-name's key (that been registered on config.py) as arg")
