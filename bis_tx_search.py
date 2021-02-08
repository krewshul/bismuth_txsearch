from tkinter import *
import tkinter as tk
import json
import requests

master = Tk()
myframe = Frame(master)
e1 = Entry(master) 
var_e1 = e1.get()
e1.grid(row = 0, column = 0, pady = 1, columnspan=4, sticky=W+E)

def TxidWindow():
    window = Toplevel()
    var_e1 = e1.get()
    url = 'http://bismuth.online/api/txid/'+var_e1
    txidinfo = requests.get(url)
    txinfo = str(txidinfo.json()[0])
    block = str(txidinfo.json()[0]['block'])
    timestamp = str(txidinfo.json()[0]['timestamp'])
    fromaddy = str(txidinfo.json()[0]['from'])
    toaddy = str(txidinfo.json()[0]['to'])
    amount = str(txidinfo.json()[0]['amount'])
    sig = str(txidinfo.json()[0]['signature'])
    txid = str(txidinfo.json()[0]['txid'])
    pubkey = str(txidinfo.json()[0]['pubkey'])
    hash = str(txidinfo.json()[0]['hash'])
    fee = str(txidinfo.json()[0]['fee'])
    reward = str(txidinfo.json()[0]['reward'])
    operation = str(txidinfo.json()[0]['operation'])
    openfield = str(txidinfo.json()[0]['openfield'])
    listbox = Listbox(window, height = 15,  
                      width = 80,  
                      bg = "black", 
                      activestyle = "dotbox",
                      font = "Courier", 
                      fg = "white")
    label = Label(window, text = " TX INFO ")
    listbox.insert(1, "block height: " + block) 
    listbox.insert(2, "timestamp: " + timestamp) 
    listbox.insert(3, "from: " + fromaddy) 
    listbox.insert(4, "to: " + toaddy) 
    listbox.insert(5, "amount: " + amount) 
    listbox.insert(6, "signature: " + sig) 
    listbox.insert(7, "pubkey: " + pubkey) 
    listbox.insert(8, "hash: " + hash)
    listbox.insert(9, "fee: " + fee)
    listbox.insert(10, "reward: " + reward)
    listbox.insert(11, "operation: " + operation)
    listbox.insert(12, "openfield: " + openfield)
    label.pack() 
    listbox.pack()


 
    
def NewWindow():
    window = Toplevel()
    url = 'http://bismuth.online/api/node/blocklast'
    blocklast = requests.get(url)
    blockheight = str(blocklast.json()['block_height'])
    timestamp = str(blocklast.json()['timestamp'])
    address = str(blocklast.json()['address'])
    recipient = str(blocklast.json()['recipient'])
    amount = str(blocklast.json()['amount'])
    sig = str(blocklast.json()['signature'])
    publickey = str(blocklast.json()['public_key'])
    blockhash = str(blocklast.json()['block_hash'])
    fee = str(blocklast.json()['fee'])
    reward = str(blocklast.json()['reward'])
    operation = str(blocklast.json()['operation'])
    nonce = str(blocklast.json()['nonce'])
    listbox = Listbox(window, height = 15,  
                      width = 80,  
                      bg = "black", 
                      activestyle = "dotbox",  
                      font = "Courier", 
                      fg = "white")
    label = Label(window, text = " Last Reported Block ")
    listbox.insert(1, "block height: " + str(blockheight)) 
    listbox.insert(2, "timestamp = " + str(timestamp))
    listbox.insert(3, "address = " + str(address))
    listbox.insert(4, "recipient = " + str(recipient))
    listbox.insert(5, "amount = " + str(amount))
    listbox.insert(6, "nonce = " + str(nonce))
    listbox.insert(7, "operation = " + str(operation))
    listbox.insert(8, "blockhash = " + str(blockhash))
    listbox.insert(9, "fee = " + str(fee))
    listbox.insert(10, "reward = " + str(reward))
    label.pack() 
    listbox.pack() 



quitbutton = tk.Button(master, 
                       text='Quit',
                       background="black", 
                       fg="white", 
                       command=master.quit).grid(row=3, 
                                                 column=0, 
                                                 sticky=tk.W, 
                                                 pady=1)
blockbutton = tk.Button(master,
                        text="LAST BLOCK",
                        background="black", 
                        fg="white", 
                        command=NewWindow).grid(row=3,
                                               column=3, 
                                               sticky=tk.W, 
                                               pady=1)
txidbutton = tk.Button(master,
                       text="TXID SEARCH",
                       background="black", 
                       fg="white", 
                       command=TxidWindow).grid(row=3,
                                               column=2, 
                                               sticky=tk.W, 
                                               pady=1) 
mainloop() 
