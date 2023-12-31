import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


project_name = "mlProject"


list_of_files = [
    f".github/workflows/.gitkeep",

    f"src/__init__.py",
    f"src/components/__init__.py",
    f"src/components/data_ingestion.py",
    f"src/components/data_transformation.py",
    f"src/components/model_training.py",
    f"src/components/model_evalution.py",
    f"src/pipeline/__init__.py",
    f"src/pipeline/training_pipeline.py",
    f"src/pipeline/prediction_pipeline.py",
    f"src/utils/__init__.py",
    f"src/utils/common.py",
    f"src/utils/common.py",
    f"src/logger.py",
    f"src/exception.py",

    f"tests/unit/__init__.py",
    f"tests/integration/__init__.py",

    f"artifacts/"
    
    f"main.py",
    f"app.py",

    f"requirements_prod.txt",
    f"requirements_dev.txt",

    f"setup.py",
    f"setup.cfg",
    f"pyproject.toml",
    f"tox.ini",
    f"experiment/experiments.ipynb"

]




for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)


    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    else:
        logging.info(f"{filename} is already exists")