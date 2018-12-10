#!/usr/bin/python3.6

import requests as rq

def get_btc():
    url = 'https://yobit.net/api/2/btc_usd/ticker'
    response = rq.get(url).json()
    rate = response['ticker']['last']
    return str(rate) + ' usd per 1 btc'
