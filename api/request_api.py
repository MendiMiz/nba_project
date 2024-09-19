import requests

def request_data(url):
    res = requests.request('GET', url)
    return res.json()