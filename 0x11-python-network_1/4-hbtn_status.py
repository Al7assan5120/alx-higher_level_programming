#!/usr/bin/python3
# Python script that fetches https://alx-intranet.hbtn.io/status


import requests

if __name__ == '__main__':
    respons = requests.get("https://alx-intranet.hbtn.io/status")
    types = type(respons.text)


print(f"Body response:\n\t- type: {types}\n\t- content: {respons.text}")
