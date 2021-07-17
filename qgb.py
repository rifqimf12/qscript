#!/usr/bin/env python3
import os
from pathlib import Path

if Path("go.mod").is_file():
    commandprefix = ""
else:
    commandprefix = "GO111MODULE=off "

os.system(f"{commandprefix}go build")
