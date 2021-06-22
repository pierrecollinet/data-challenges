# pylint: disable=no-value-for-parameter
"""
Client of the Wagon OpenGraph API
"""


import requests
import json

def fetch_metadata(url):
    """
    Return a dictionary of OpenGraph metadata found in HTML of given url
    """
    requested_url = "https://opengraph.lewagon.com/?url=" + url
    response_API = requests.get(requested_url)
    if response_API.status_code == 200:
        data = response_API.text
        parse_json = json.loads(data)
        return parse_json["data"]
    return None

# To manually test, please uncomment the following lines and run `python opengraph.py`:
import pprint
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(fetch_metadata("https://www.lewagon.com"))
