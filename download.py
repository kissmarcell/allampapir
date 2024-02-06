import requests
import os
from datetime import date
import time
import json

PAPER_TYPES_REQUEST: str = "https://www.allampapir.hu/api/network_rate/m/get_papers"
PAPER_DATA_REQUEST: str = "https://www.allampapir.hu/api/network_rate/m/get_prices/{}"
DATA_FOLDER_NAME: str = "data"

for key in requests.get(PAPER_TYPES_REQUEST).json()["data"].keys():
    folder_path: str = os.path.join(os.getcwd(), DATA_FOLDER_NAME, key)
    if not os.path.exists(folder_path) or not os.path.isdir(folder_path):
        os.makedirs(folder_path)
    file_path: str = os.path.join(folder_path, f"{date.today()}_{int(time.time())}.json")
    with open(file_path, "w") as f:
        paper: dict = requests.get(PAPER_DATA_REQUEST.format(key)).json()
        json.dump(paper["data"]["data"], f)
