#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import numpy as np
import pandas as pd
from termcolor import colored
from time import sleep

# data source
from yahoo_fin import stock_info as si

# need to set a previous out of scope
previous_price = 0.0
highest = 0.0
start_price = si.get_live_price("GME")
lowest = start_price

# infinite loop
while(True):
    try:
        current_price = si.get_live_price("GME")  # get most recent price
    except:
        continue
    if current_price < lowest:
        lowest = current_price
    if current_price > highest:
        highest = current_price

    if current_price != previous_price:
        if current_price > start_price:
            os.system('clear') # clear terminal
            print("GME: {}".format(colored(current_price, 'green', attrs=['bold',])))
        else:
            os.system('clear')
            print("GME: {}".format(colored(current_price, 'red')))
        print("low: {}\t\thigh: {}".format(lowest, highest))
        previous_price = current_price
    elif current_price == previous_price:
        sleep(1)  # sleep to allow price to change saves on bandwidth usage
        continue


