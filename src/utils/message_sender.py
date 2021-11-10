from flask.json.tag import PassList
import requests
import json


def send_message(payload):

    url = "https://rapidapi.rmlconnect.net/wbm/v1/message"
    payload = json.dumps(payload)
    headers = {
    'Authorization': '617bf20f245383001100f817',
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)
