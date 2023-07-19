#!/usr/bin/python3
"""
*Python script that takes in a URL and an email address,
 sends a POST request to the passed URL with the
 email as a parameter, and finally displays the body of the response.
*Email must be sent in the variable email
*Must use the packages requests and sys
*Dot allowed to import packages other than requests and sys
*Don’t need to error check arguments passed to the script (number or type)
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}

    r = requests.post(url, data=value)
    print(r.text)
