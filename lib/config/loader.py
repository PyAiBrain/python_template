import json
import os

CONFIG_PATH: str = os.path.join(os.path.dirname(__file__), "config.jsonc")

def load_config() -> dict:
    """Lädt die Konfigurationsdatei."""
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

CONFIG: dict = load_config()
