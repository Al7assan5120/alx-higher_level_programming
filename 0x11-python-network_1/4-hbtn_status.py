#!/usr/bin/python3
# Python script that fetches https://alx-intranet.hbtn.io/status


import requests

if __name__ == '__main__':
    respons = requests.get("https://alx-intranet.hbtn.io/status")
    print(f"Body response:\n\t- type: {type(respons.text)}\n\t- content: {respons.text}")
