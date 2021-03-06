#activate virtual environment and install modules

import os
from sys import platform

def activate_env():
    #windows
    if platform == "win32":
        os.system(".\\venv\Scripts\\activate.bat")

    #mac or linux
    if platform == "darwin" or platform == "linux" or platform == "linux2":
        os.system("source ./venv/bin/activate")


    os.system("pip install -r requirements.txt")