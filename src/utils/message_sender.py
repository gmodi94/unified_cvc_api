import requests


def send_message(payload,number,name):
    payload.format(number,name)
    