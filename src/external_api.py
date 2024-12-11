import os

import requests
from dotenv import load_dotenv
from requests import RequestException

load_dotenv("../.env")
API_KEY = os.getenv("API_KEY")


