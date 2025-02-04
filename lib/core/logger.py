import logging
import os
from lib.config.loader import CONFIG

COLORS = CONFIG.get("logging", {}).get("colors", {})

class ColoredFormatter(logging.Formatter):
    def format(self, record):
        color = COLORS.get(record.levelname, "")
        reset = COLORS.get("RESET", "")
        return f"{color}{super().format(record)}{reset}"

def setup_logger():
    log_format = CONFIG["logging"]["format"]
    log_file = CONFIG["paths"]["log_file"]

    os.makedirs(os.path.dirname(log_file), exist_ok=True)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(ColoredFormatter(log_format))

    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(logging.Formatter(log_format))

    logger = logging.getLogger("MyApp")
    logger.setLevel(CONFIG["logging"]["level"].upper())
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    
    return logger

LOG = setup_logger()
