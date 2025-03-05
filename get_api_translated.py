import requests


def get_api_translated(url):
    response = requests.get(url)
    for r in response.json()["matches"]:
        return r['translation']
