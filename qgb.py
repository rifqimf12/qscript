#!/usr/bin/env python3
import os
from qtools import getGoModuleOption


os.system(f"{getGoModuleOption()}go build")
