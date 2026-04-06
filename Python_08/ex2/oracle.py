from dotenv import load_dotenv
import os
from typing import Any


if __name__ == "__main__":

    if load_dotenv() is not True:
        print("ERROR: .env file found")

    matrix_Mode: Any = os.getenv("MATRIX_MODE")
    database_url: Any = os.getenv("DATABASE_URL")
    api_key: Any = os.getenv("API_KEY")
    log_level: Any = os.getenv("ZION_ENDPOIN")

    list_config: list = [matrix_Mode,
                         database_url,
                         api_key,
                         log_level]

    if not list_config:
        print("ERROR: no value, edit .env with your values")
        

