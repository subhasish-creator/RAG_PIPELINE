import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')
project_name='RAG'

list_of_files=[
    ".github/workflows/.gitkeep",
    f"{project_name}/__init__.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/utils/__init__.py",
    f"{project_name}/config/__init__.py",
    f"{project_name}/config/config.yaml",
    f"{project_name}/data/data.txt",
    f"{project_name}/modules/__init__.py",
    f"{project_name}/modules/data_loader.py",
    f"{project_name}/modules/vector_store.py",
    f"{project_name}/modules/query_engine.py",
    f"{project_name}/modules/config_loader.py",
    f"{project_name}/storage",
    "requirements.txt",
    "README.md",
    ".env",
    "app.py",
    "main.py",
    "setup.py",
    "code/trial.ipynb",
    "templates/index.html",
    "static/style.css",
    "test.py"

]
for file_path in list_of_files:
    # Create directories if they don't exist
    directory = os.path.dirname(file_path)
    if directory != "":
        os.makedirs(directory, exist_ok=True)

    # Create file with placeholder if not exist
    if not os.path.exists(file_path):
        with open(file_path, "w") as f:
            content = f"# Auto-generated: {file_path}" if file_path.endswith(".py") else ""
            f.write(content)
        print(f"✅ Created: {file_path}")
    else:
        print(f"⚠️ Already exists: {file_path}")
        

