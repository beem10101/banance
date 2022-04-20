import socket
from symtable import Symbol
from dotenv import load_dotenv
from binance import Client,ThreadedWebsocketManager
from pprint import pprint
import os
load_dotenv()

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((socket.gethostname(),1234))
server.listen(5)

api_key = os.environ.get("api_key")
api_secret = os.environ.get("api_secret")
client = Client(api_key,api_secret)
info = client.get_account()
price = client.get_all_tickers()
clientsocket, address = server.accept()

def Search(x) :
    for i in price :
        if i['symbol'] == x.upper():
            return i['price']
    else:
        return 'not found'

while True :
    string = clientsocket.recv(1024)
    # print(f"connection{address}")
    if not string or (string.decode('utf-8')) == "2." or (string.decode('utf-8')) == "2" :
        print(f"Exited by client{address}")
        break
    try:
        string = string.decode("utf-8")
        clientsocket.send(bytes(Search(string),"utf-8"))
    except:
        print(f"Exited by client{address}")

