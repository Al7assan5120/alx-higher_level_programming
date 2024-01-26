#!/usr/bin/python3
# Python script that fetches https://alx-intranet.hbtn.io/status


import urllib
import sys
from urllib.request import urlopen

if __name__ == "__main__":
    with urlopen(sys.argv[1]) as response:
        request_id = response.getheader("X-Request-Id")
        response.close()

    print(request_id)
