import os
from dotenv import load_dotenv
from pathlib import Path

# read .env file
load_dotenv(dotenv_path=Path(__file__).parent.parent / ".env", encoding="utf-8")

class Config:
    DB_NAME = os.getenv('DB_NAME')
    DB_HOST = os.getenv('DB_HOST')
    DB_USER = os.getenv('DB_USER')
    DB_PASS = os.getenv('DB_PASS')
    DB_PORT = os.getenv('DB_PORT')

# create instance config
config = Config()
