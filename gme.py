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

# infinite loop
while(True):
    current_price = si.get_live_price("GME")  # get most recent price
    if current_price != previous_price:
        if current_price > previous_price:
            os.system('clear') # clear terminal
            print("GME: {}".format(colored(current_price, 'green', attrs=['bold',])))
        else:
            os.system('clear')
            print("GME: {}".format(colored(current_price, 'red')))
        previous_price = current_price
    elif current_price == previous_price:
        sleep(5)  # sleep to allow price to change saves on bandwidth usage
        continue


