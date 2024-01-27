#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8)"""

import requests
from requests.exceptions import HTTPError
import sys

if __name__ == '__main__':

    url = sys.argv[1]

    try:
        body = requests.get(url)
        print(body)
    except HTTPError as error:
        print(f'Error code: {body.status_code}')
