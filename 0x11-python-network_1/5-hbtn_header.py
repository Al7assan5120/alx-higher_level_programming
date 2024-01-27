#!/usr/bin/python3
"""Write a Python script that takes in a URL, sends a request
to the URLand displays the value of the variable X-Request-Id
in the response header"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    req = requests.get(url)
    request_id = req.headers.get("X-Request-Id")
    print(request_id)
