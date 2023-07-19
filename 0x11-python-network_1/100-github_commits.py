#!/usr/bin/python3
"""
*Python script that takes 2 arguments in order to solve this challenge.
*First argument will be the repository name
*Second argument will be the owner name
*Must use the packages requests and sys
*Dot allowed to import packages other than requests and sys
*Don’t need to check arguments passed to the script (number or type)
"""
import sys
import requests


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])

    response = requests.get(url)
    commits = response.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                commits[i].get("sha"),
                commits[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
