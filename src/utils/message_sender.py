from flask.json.tag import PassList
import requests
import json


def send_message(payload,channel,phonenumber=None):
    if channel == "wbm":
        url = "https://rapidapi.rmlconnect.net/wbm/v1/message"
        payload = json.dumps(payload)
        headers = {
        'Authorization': '617bf20f245383001100f817',
        'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        print(response.text)
    elif channel == "sms":
        r = requests.get('https://rapidapi.rmlconnect.net:9443/bulksms/bulksms',params={'username': 'rapid-4z6z719010000','password':'617bf20f245383001100f817','type':'0','dlr':'0','destination':phonenumber,'source':'RMLPRD','message':payload})
        print(r.text)



