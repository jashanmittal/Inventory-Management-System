import time
import random
import json
import datetime

class Product():
    def __int__(self, item, quantity, price):
        self.item = item
        self.quantity = quantity
        self.price = price

    def display(self):
        print(f"""
------------------------
Item : {self.item}
Price : {self.price}
Quantity : {self.quantity}
------------------------""")
        
    
class Customer():
    def __init__(self, name, password, balance):
        self.name = name
        self.password = password
        self.balance = balance
    
    
