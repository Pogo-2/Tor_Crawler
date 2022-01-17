from misc.Init_functions import *
from misc.url_checkers import *
import requests

# get config and init vars
config = parse_config("./config.json")
starting_list = config["starting_tor_list"]
con_list = []
tor_list = []

# create connection list
for n_con in range(config["num_bots"]):
    con_list.append(requests)

# turn all strings in the tor_list to WebPage
tor_list.extend(string_to_website(starting_list, con_list[0]))

# start the looping process
while len(tor_list) >= 0:
    for website in tor_list:
        new_url_list = website.scrape_site()
        ws_list = string_to_website(new_url_list, con_list[0])

        for url in ws_list:
            url.scrape_site()
        pass
    # todo check sql for string
    # todo if string is found then continue else save to sql
