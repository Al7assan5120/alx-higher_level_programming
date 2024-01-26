#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL
and displays the value of the X-Request-Id variable
found in the header of the response"""

import urllib
import sys
from urllib.request import urlopen

if __name__ == "__main__":
    with urlopen(sys.argv[1]) as response:
        request_id = response.getheader("X-Request-Id")
        print(request_id)
