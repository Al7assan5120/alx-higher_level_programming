#!/usr/bin/python3
"""Python script that takes in a URL and an email, sends a POSTrequest
to the passedURL with the email as a parameter, and displays
the body of the response (decoded in utf-8"""

import urllib
import sys
from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from urllib import parse

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with urlopen(url) as response:
            print(response.read().encode("utf-8"))
    except HTTPError as error:
        print(f'Error code: {error.status}')
