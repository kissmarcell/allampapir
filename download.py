import requests
import os
from datetime import date
import json

PAPER_TYPES_REQUEST: str = "https://www.allampapir.hu/api/network_rate/m/get_papers"
PAPER_DATA_REQUEST: str = "https://www.allampapir.hu/api/network_rate/m/get_prices/{}"
DATA_FOLDER_NAME: str = "data"

for bond_type in requests.get(PAPER_TYPES_REQUEST).json()["data"].keys():
    all_bonds_by_type: dict = requests.get(PAPER_DATA_REQUEST.format(bond_type)).json()["data"]["data"]
    for bond in all_bonds_by_type:
        folder_path: str = os.path.join(os.getcwd(), DATA_FOLDER_NAME, bond_type, bond["longName"])
        os.makedirs(folder_path, exist_ok=True)
        file_path: str = os.path.join(folder_path, f"{date.today()}.json")
        if not os.path.exists(file_path):
            with open(file_path, "w") as f:
                json.dump(bond, f)
