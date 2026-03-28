import json
from datetime import data 
import logging

logger = logging.getLogger(__name__)

def load_data():
    file_path = f"./data/yt_data_{data}.json"

    try:
        logger.info(f"Processing file: YT_data{data.today()}")

        with open(file_path, "r", encoding="utf-8") as raw_data:
            data = json.load(raw_data)
        return data
    except FileNotFoundError:
        logger.error(f"File not found: {file_path}")
        raise   
    except json.JSONDecodeError:
        logger.error(f"Invalid JSON in file: {file_path}")
        raise