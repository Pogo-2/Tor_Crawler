import json
from stem.control import Controller
import requests

# global vars
proxies = {
    'http': 'socks5://127.0.0.1:9050',
    'https': 'socks5://127.0.0.1:9050'
}


def parse_config(path):
    return json.loads(open(path).read())


def auth_stem():
    with Controller.from_port(port= 9051) as c:
        c.authenticate()

def check_ip(connection, Proxies=True):
    if Proxies:
        return connection.get('https://ident.me', proxies=proxies).text
    else:
        return connection.get('https://ident.me').text





