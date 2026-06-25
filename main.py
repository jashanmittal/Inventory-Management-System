import time
import random
import json
import datetime

accounts = []
stock = []

class Product():
    def __init__(self, item, quantity, price):
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
    def __init__(self, name="", password="", acc_num=0, balance=0):
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
        customer = Customer(self.name, self.password, self.acc_num, 0)
        accounts.append(customer)

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

class Admin():
    def __init__(self):
        pass
    
    def add_product(self):
        item_name = input("Name of item : ")
        item_price = float(input("Enter item's price : "))
        item_quantity = int(input("Enter quantity : "))

        product = Product(item_name, item_quantity, item_price)
        stock.append(product)

        print("Successfully added the product")

    def remove_product(self):
        for index, product in enumerate(stock, start=1):
            print(f"""
---------------------------------
{index}. Item : {product.item}
Price : {product.price}
Quantity : {product.quantity}
---------------------------------""")
            
        try:
            choice = int(input("Which would you like to delete? "))
        except ValueError:
            print("Enter Valid Value")
            return
        
        if 1 <= choice <= len(stock):
            stock.pop(choice - 1)
            print("Deleted Successfully")

        else:
            print("Product Not Found")

    def check_users(self):
        for index, account in enumerate(accounts, start=1):
            print(f"""
----------------------------------------
{index}. Name : {account.name}
Balance : {account.balance}
Account Number : {account.acc_num}
----------------------------------------""")
            
    
def menu():
    while True:
        print("Which feature would you like to use:")
        print("1. Register\n" \
        "2. Login\n" \
        "3. Exit")
        choice = input()

        if choice == "1":
            new_acc = Customer()
            new_acc.register()
            time.sleep(1)

        elif choice == "2":
            acc_num = int(input("Enter your account number : "))
            found = False
            for acc in accounts:
                if acc.acc_num == acc_num:
                    acc.login()
                    found = True
                    break
            if not found:
                print("Account Number Not Found")

        elif choice == "3":
            exit()

        else:
            print("Invalid Command")

menu()
        