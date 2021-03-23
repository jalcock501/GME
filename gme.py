#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import numpy as np
import pandas as pd
from termcolor import colored
from time import sleep

# data source
from yahoo_fin import stock_info as si


previous_price = 0.0

while(True):
    current_price = si.get_live_price("GME")
    if current_price != previous_price:
        if current_price > previous_price:
            os.system('clear')
            print("GME: {}".format(colored(current_price, 'green', attrs=['bold',])))
        else:
            os.system('clear')
            print("GME: {}".format(colored(current_price, 'red')))
        previous_price = current_price
    elif current_price == previous_price:
        sleep(5)
        continue


