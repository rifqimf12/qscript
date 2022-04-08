#!/usr/bin/env python3
import os
import sys
from qtools import (
    createLogFile,
    readEnvsFromDockerYML,
    exportEnvs,
    curdir,
    getGoModuleOption,
)


args = sys.argv
if len(args) > 1:
    if args[1] == "f":
        env = "factory"
    elif args[1] == "d":
        env = "dev"
    elif args[1] == "a":
        env = "assembly"
    else:
        env = args[1]
    if args[1] == "0":
        isExportingEnv = False
    else:
        isExportingEnv = True
else:
    env = "dev"

if isExportingEnv:
    exportEnvs(
        readEnvsFromDockerYML(
            f"docker/docker-compose.{env}.yml", "services", curdir(), "environment"
        )
    )

logFileName = createLogFile()
command = (
    f"code {logFileName} && {getGoModuleOption()}go run *.go 2>&1 | tee {logFileName}"
)
# print(command)
os.system(command)
