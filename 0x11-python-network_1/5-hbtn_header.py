#!/usr/bin/python3
"""
*Python script that takes in a URL, sends a request to the URL
 and displays the value of the variable X-Request-Id in the response header
*Must use the packages requests and sys
*Not allow to import other packages than requests and sys
*The value of this variable is different for each request
*Don’t need to check script arguments (number and type)
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    response = requests.get(url)
    print(response.headers.get("X-Request-Id"))
