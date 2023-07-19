#!/usr/bin/python3
"""
*Python script that takes in a URL,
 sends a request to the URL and displays the value of
 the X-Request-Id variable found in the header of the response.
*Must use the packages urllib and sys
*Not allow to import packages other than urllib and sys
*Value of this variable is different for each request
*Don’t need to check arguments passed to the script (number or type)
*Must use a with statement
"""
import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))
