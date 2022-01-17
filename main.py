from misc.Init_functions import *
from stem.control import Controller

config = parse_config("./config.json")
tor_list = config["starting_tor_list"]

auth_stem()

r = requests.get(tor_list[0], proxies=proxies)
pass
