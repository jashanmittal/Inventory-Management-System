import time
import random
import json
import datetime

accounts = []

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
    def __init__(self, name, password, acc_num, balance=0):
        self.name = name
        self.password = password
        self.acc_num = acc_num
        self.balance = balance
    
    def register(self):
        self.name = input("Enter your name : ")
        self.password = input("Enter the password : ")
        while True:
            number = random.randint(100,999)
            found = False
            for acc in accounts:
                if acc.acc_num == number:
                    found = True
                    break

            if not found:
                self.acc_num = number
                break
            print(f"Your Account Number is {self.acc_num}")

    def login(self):
        name = input("Enter your name : ")
        password = input("Enter your password : ")

        if name == self.name and password == self.password:
            print("Sucessfully Logged In")
        elif name != self.name:
            print("Invalid Name")
        elif password != self.password:
            print("Invalid Password")
        else:
            print("Invalid name and password")

