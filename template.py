import os
from pathlib import Path
import logging

logging.basicConfig(
    level=logging.INFO,
    format= "[%(asctime)s : %(levelname)s] %(message)s"
    )

while True:
    project_name = input("Enter the name of the project : ")
    if project_name != "":
        break

logging.info(f"Creatinf project name by {project_name}")

list_of_files = [
    f"src/{project_name}/__init__.py",
    #"tests/__init__.py",    #Default test file
    #"tests/unit/__init__.py",   #Dummy test available
    #"tests/integration/__init__.py",    #Dummy test available
    #"init_setup.sh",    #Change as per need
    #requirements.txt", #Basic requirements
    #"requirements_dev.txt", #Dev testing
    #"setup.py", #Change as of need
    #"pyprojecct.toml",  
    #"setup.cfg",
    #"tox.ini" #Testing on various environments
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory at : {filedir} for file : {filename}")
    if (not os.path.exists(filepath) or (os.path.getsize(filepath) == 0)):
        with open (filepath, "w"):
            pass
        logging.info(f"Creating a new file : {filedir} at path : {filepath}")

    else:
        logging.info(f"File is already present in {filepath}")
        