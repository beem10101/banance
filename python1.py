from symtable import Symbol
from dotenv import load_dotenv
from binance import Client,ThreadedWebsocketManager
from pprint import pprint
import os
import socket
load_dotenv()
input1 = str(input())
input2 = str(input())
n = input1+input2
api_key = os.environ.get("api_key")
api_secret = os.environ.get("api_secret")
client = Client(api_key,api_secret)
info = client.get_account()
# pprint(client.get_account())
# for i in info :
#     print(i)

price = client.get_all_tickers()
# pprint(price)
def Search(x) :
    for i in price :
        if i['symbol'] == x.upper():
            return i['price']
    else:
        return 'not found'
print(Search(n))


# bal = info['balances']
# for i in bal :
#     if float(i['free']) > 0 :
#         pprint(i)

