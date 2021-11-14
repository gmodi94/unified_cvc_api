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
    elif channel == "rcs":
        url = "https://rapidapi.rmlconnect.net/rcs/v1/message"
        payload = json.dumps(payload)
        headers = {
        'Authorization': '617bf20f245383001100f817',
        'Content-Type': 'application/json'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        print(response.text)

    elif channel == "mail":
        url = "https://rapidemail.rmlconnect.net/v1.0/messages/sendMail"
        headers = {
        'Content-Type': 'application/json'
        }
        response = requests.request("POST", url, headers=headers, data=payload)


def capability(mobile_number):
    url = "https://rapidapi.rmlconnect.net/wbm/bot/v1/contactCapabilities"
    payload = json.dumps({
    "contacts": [
        mobile_number
    ]
    })
    headers = {
    'Authorization': '617bf20f245383001100f817',
    'Content-Type': 'application/json'
    }
    try:
        response = requests.request("POST", url, headers=headers, data=payload)
        response = json.loads(response.text)
        if isinstance(response,str):
            response = json.loads(response)
            if response["result"][0]["status"] == "valid":
                return True
            else:
                return False
        else:
            if response["result"][0]["status"] == "valid":
                return True
            else:
                return False

    except:
        return False
