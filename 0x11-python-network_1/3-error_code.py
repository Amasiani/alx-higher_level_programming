#!/usr/bin/python3
"""
*Python script that takes in a URL, sends a request to the URL
 and displays the body of the response (decoded in utf-8).
*You have to manage urllib.error.HTTPError exceptions and print:
 Error code: followed by the HTTP status code
*Must use the packages urllib and sys
*Not allowed to import other packages than urllib and sys
*Don’t need to check arguments passed to the script (number or type)
*Must use the with statement
"""


if __name__ == "__main__":
    import sys
    from urllib import request, error

    try:
        with request.urlopen(sys.argv[1]) as res:
            print(res.read().decode('UTF-8'))
    except error.HTTPError as er:
        print('Error code:', er.code)
