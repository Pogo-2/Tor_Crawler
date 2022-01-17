import json
from stem.control import Controller
from stem import Signal
from misc.WebSite import WebSite
import asyncio

# global vars
proxies = {
    'http': 'socks5://127.0.0.1:9050',
    'https': 'socks5://127.0.0.1:9050'
}


def parse_config(path):
    return json.loads(open(path).read())


def update_ip():
    with Controller.from_port(port=9051) as c:
        c.authenticate()
        c.signal(Signal.NEWNYM)


def check_ip(connection, p=True):
    if p:
        return connection.get('https://ident.me', proxies=proxies).text
    else:
        return connection.get('https://ident.me').text


def string_to_website(my_list, connection):
    ws_list = []
    for url in my_list:
        try:
            r = connection.get(url).content
            ws_list.append(WebSite(url, r))
        except:
            continue
    return ws_list



