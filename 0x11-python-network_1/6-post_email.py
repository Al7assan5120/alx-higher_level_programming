#!/usr/bin/python3
"""Write a Python script that takes in a URL and an email
address, sends a POST request to the passed URLwith the email
as a parameter, and finally displays the body of the response."""

import requests
from sys import argv

if __name__ == '__main__':

    url = argv[1]
    data = {"email": argv[2]}

    post = requests.post(url, data=data)
    print(post.text)
