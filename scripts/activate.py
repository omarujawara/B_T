import os
from sys import platform

#windows
if platform == "win32":
    os.system("../venv/bin/activate")

 #mac or linux
if platform == "darwin" or platform == "linux" or platform == "linux2":
    os.system("..\venv\Scripts\activate.bat")

os.system("pip install -r requirements.txt")