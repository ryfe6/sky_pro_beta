import json
from typing import Any

import pandas as pd

from src.logger import setup_logging


def get_read_file_csv_or_xlsx(filename: str) -> Any:
    logger.info("Start get_read_file_csv_or_xlsx")
    if ".csv" in filename:
        wine_reviews = pd.read_csv(filename)
        logger.info("Finished read file csv")
        return wine_reviews
    elif ".xlsx" in filename:
        wine_reviews = pd.read_excel(filename)
        logger.info("Finished read file xlsx")
        return wine_reviews
    elif ".json" in filename:
        with open(filename, "r", encoding="utf8") as file:
            data_json = json.load(file)
            logger.info("Finished read file json")
            return data_json
    logger.info("Finished None")
    return "Что то пошло не так"


logger = setup_logging()
