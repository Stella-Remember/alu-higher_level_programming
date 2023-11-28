#!/usr/bin/python3
"""Fetches https://alu-intranet.hbtn.io/status"""

from urllib import request

url = "https://alu-intranet.hbtn.io/status"

with request.urlopen(url) as response:
    content = response.read()
    print("Body response:")
    print(f"\t- type: {type(content)}")
    print(f"\t- content: {content}")
    print(f"\t- utf8 content: {content.decode('utf-8')}")
