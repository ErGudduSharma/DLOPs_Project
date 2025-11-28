import os   # to handle file paths and directories
from pathlib import Path   # to handle file system paths in an object-oriented way
import logging   # to log messages for tracking the execution flow

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')      # Configure logging to display info level messages with timestamps


project_name = "cnnClassifier"   # Define the project name

list_of_files = [
        ".github/workflows/.gitkeep",       # GitHub Actions workflow directory
        f"src/{project_name}/__init__.py",  # Source directory for the project
        f"src/{project_name}/components/__init__.py", # Components subdirectory
        f"src/{project_name}/utils/__init__.py", # Utilities subdirectory
        f"src/{project_name}/config/__init__.py", # Configuration subdirectory
        f"src/{project_name}/config/configuration.py", # Configuration file for the project
        f"src/{project_name}/pipeline/__init__.py", # Pipeline ka use hm kr rhe h data flow k liye or model training k liye
        f"src/{project_name}/entity/__init__.py", # Entity subdirectory for data models
        f"src/{project_name}/constants/__init__.py", # Constants subdirectory for fixed values
        "config/config.yaml", # kha se data aa rha h, kha pr unzip hoga 
        "dvc.yaml", #data version control...ye text ko control krta h values ko nhi krta
        "params.yaml", # pre-training parameters(epochs, batch size, learning rate etc)
        "requirements.txt", # project dependencies
        "setup.py", # iss application ko package formate me convert krne k liye
        "research/trials.ipynb", # jupyter notebook for research and experimentation for testing purpose
        "templates/index.html" # HTML template file for web interface (ui/ux)

                ]

# ydi file ya directory exist nhi krti to create krdo otherwise skip krdo
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)


    if filedir !="": # if filedir is not empty
        os.makedirs(filedir, exist_ok=True)  # exist_of = True....Create directory if it doesn't exist
        logging.info(f"Creating directory; {filedir} for the file: {filename}") # log the creation of the directory

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0): # if file doesn't exist or file is empty
        with open(filepath, "w") as f: # create an empty file and open it in write mode
            pass
            logging.info(f"Creating empty file: {filepath}") #


    else:
        logging.info(f"{filename} is already exists")