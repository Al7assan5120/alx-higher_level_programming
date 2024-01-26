#!/usr/bin/python3
"""Python script that takes in a URL and an email, sends a POSTrequest
to the passedURL with the email as a parameter, and displays
the body of the response (decoded in utf-8"""

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
