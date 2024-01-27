#!/usr/bin/python3
# Python script that fetches https://alx-intranet.hbtn.io/status


import requests

respons = requests.get("https://alx-intranet.hbtn.io/status")
types = type(respons)


print(f"Body response:\n\t- type: {types}\n\t- content: {respons}")
