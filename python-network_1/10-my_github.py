#!/usr/bin/python3
"""Displays the GitHub id of a user using Basic Authentication."""
import requests
import sys


if __name__ == "__main__":
    auth = (sys.argv[1], sys.argv[2])
    r = requests.get('https://api.github.com/user', auth=auth)
    print(r.json().get('id'))
