#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL
and displays the value of the X-Request-Id variable
found in the header of the response"""

import urllib
import sys
from urllib.request import urlopen
from urllib import parse

if __name__ == "__main__":
    url = sys.argv[1]
    value = {'email': sys.argv[2]}
    data = parse.urlencode(value).encode("utf-8")
    with urlopen(url, data) as response:
        print(response.read().encode("utf-8"))
