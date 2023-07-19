#!/usr/bin/python3
"""
*Python script that takes your GitHub credentials (username and
 password) and uses the GitHub API to display your id
*Must use Basic Authentication with a personal access token as
 password to access to your information (only read:user permission is needed)
*The first argument will be your username
*The second argument will be your password
 (in your case, a personal access token as password)
*Must use the package requests and sys
*Not allowed to import packages other than requests and sys
*You don’t need to check arguments passed to the script (number or type)
"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    response = requests.get("https://api.github.com/user", auth=auth)
    print(response.json().get("id"))
