from urllib import response

import requests
from datetime import *

USERNAME = "kdbburns"
TOKEN = "Kjlsghtin&881*"
GRAPH_ID = "graph1"

pixela_enpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_enpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_enpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Water Consumption",
    "unit": "L",
    "type": "int",
    "color": "shibafu"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_creation_endpoint = f"{pixela_enpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "4",
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)




