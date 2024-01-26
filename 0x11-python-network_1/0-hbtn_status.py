#!/usr/bin/python3
# Python script that fetches https://alx-intranet.hbtn.io/status


import urllib
from urllib.request import urlopen

with urlopen("https://alx-intranet.hbtn.io/status") as respons:
    body = respons.read()
    types = type(body)
    charset = respons.headers.get_content_charset()
    respons.close()

print((f"Body response:\n\t- type: {types}\n\t- content: {body}\n"
       f"\t- utf8 content: {charset}"))
