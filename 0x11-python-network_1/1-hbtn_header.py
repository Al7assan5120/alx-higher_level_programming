#!/usr/bin/python3
# Python script that fetches https://alx-intranet.hbtn.io/status


import urllib
import sys
from urllib.request import urlopen


with urlopen(sys.argv[1]) as respons:
    request_id = respons.headers.get('X-Request-Id')
    respons.close()

print(request_id)
