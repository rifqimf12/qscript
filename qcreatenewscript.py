#!/usr/bin/env python3
import sys, os
from qtools import getScriptDir


def createNewPythonScript(fileName):
    f = open(f"{getScriptDir()}/{fileName}", "a")
    f.write("#!/usr/bin/env python3\n")
    f.close()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        fileName = sys.argv[1]
        if fileName[:-3] != ".py":
            fileName += ".py"
        createNewPythonScript(fileName)
        os.system(f"chmod +x {fileName}")
        os.system(f"code {fileName}")
    else:
        print("pass filename as arg")
