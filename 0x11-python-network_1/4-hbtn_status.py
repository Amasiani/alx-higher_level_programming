#!/usr/bin/python3
"""
*Python script that fetches https://alx-intranet.hbtn.io/status
*Must use the package requests
*Not allow to import packages other than requests
*The body of the response must be display like
 the following example (tabulation before -)
"""
import requests


if __name__ == "__main__":
    response = requests.get('https://alx-intranet.hbtn.io/status')
    ct = response.text
    print('Body response:\n\t- type: {}\n\t- content: {}'.format(type(ct), ct))
