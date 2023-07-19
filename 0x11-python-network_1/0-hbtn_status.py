#!/usr/bin/python3
"""
*Python script that fetches https://alx-intranet.hbtn.io/status
*Must use the package urllib
*You are not allowed to import any packages other than urllib
*The body of the response must be displayed like the following
 example (tabulation before -)
*Must use a with statement
"""


if __name__ == '__main__':
    import urllib.request

    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as resp:
        content = resp.read()
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode('utf-8')))
