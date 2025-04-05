# Auto-generated: RAG/modules/config_loader.py
import yaml

def load_config(path="config/config.yaml"):
    with open(path, "r") as f:
        return yaml.safe_load(f)
