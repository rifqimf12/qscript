#!/usr/bin/env python3
import os
import yaml


def curdir():
    fullpath = os.getcwd()
    lastpath = fullpath.rsplit("/", 1)[1]
    return lastpath


def createLogFile():
    fileName = f"{curdir()}.log"
    f = open(fileName, "a")
    f.close()
    return fileName


def readEnvsFromDockerYML(fileName, *keys):
    with open(fileName, "r") as stream:
        yamlObj = yaml.safe_load(stream)
        for key in keys:
            yamlObj = yamlObj[key]
    return yamlObj


def exportEnvs(envs):
    for envKey, envValue in [env.split("=", 1) for env in envs]:
        os.environ[envKey] = envValue
