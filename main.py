import time
import random
import json
import datetime

accounts = []
stock = []


def save_data():
    with open("accounts.json", "w") as f:
        json.dump([acc.__dict__ for acc in accounts], f)
    with open("stock.json", "w") as f:
        json.dump([prod.__dict__ for prod in stock], f)

def load_data():
    global accounts, stock
    try:
        with open("accounts.json", "r") as f:
            accounts_data = json.load(f)
            accounts = [Customer(**acc) for acc in accounts_data]
    except FileNotFoundError:
        accounts = []

    try:
        with open("stock.json", "r") as f:
            stock_data = json.load(f)
            stock = [Product(**prod) for prod in stock_data]
    except FileNotFoundError:
        stock = []
    
def admin_login():
    username = input("Enter admin username : ")
    password = input("Enter admin password : ")

    if username == "admin" and password == "admin":
        print("Successfully Logged In")
        admin_menu()
    else:
        print("Invalid Username or Password")


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
        self.inventory = []
        self.transactions = []
    
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
        save_data()

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
            save_data()

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
        "3. Admin Login\n" \
        "4. Exit")
        choice = input()

        if choice == "1":
            new_acc = Customer()
            new_acc.register()
            save_data()
            time.sleep(1)

        elif choice == "2":
            acc_num = int(input("Enter your account number : "))
            found = False
            for acc in accounts:
                if acc.acc_num == acc_num:
                    acc.login()
                    main(acc)
                    found = True
                    break
            if not found:
                print("Account Number Not Found")

        elif choice == "3":
            admin_login()

        elif choice == "4":
            exit()

        else:
            print("Invalid Command")

def main(current_account):
    print("Which feature would you like to use:")
    print("1. Buy Products\n" \
    "2. Check Balance\n" \
    "3. Check Inventory\n" \
    "4. Check Transactions\n" \
    "5. Logout")
    choice = input()

    if choice == "1":
        for index, product in enumerate(stock, start=1):
            print(f"""
---------------------------------
{index}. Item : {product.item}
Price : {product.price}
Quantity : {product.quantity}
---------------------------------""")
        
        try:
            buy = int(input("Which product would you like to buy : "))
        except ValueError:
            print("Product Not Found")
        if buy < 1 or buy > len(stock):
            print("Product Not Found")
            return
        if stock[buy - 1].quantity <= 0:
            print("Product Out of Stock")
        elif current_account.balance < stock[buy - 1].price:
            print("Insufficient Balance")
        else:
            current_account.balance -= stock[buy - 1].price
            stock[buy - 1].quantity -= 1
            print("Purchase successful")
            transaction.append(f"Bought {stock[buy - 1].item} for {stock[buy - 1].price} on {datetime.datetime.now()}")
            save_data()
            time.sleep(1)

    elif choice == "2":
        print(f"Your balance is {current_account.balance}")
        time.sleep(1)

    elif choice == "3":
        for index, product in enumerate(current_account.inventory, start=1):
            print(f"""---------------------------------
{index}. Item : {product.item}
Price : {product.price}
Quantity : {product.quantity}
---------------------------------""")
        time.sleep(1)

    elif choice == "4":
        for index, transaction in enumerate(current_account.transactions, start=1):
            print(f"{index}. {transaction}")
        time.sleep(1)

    elif choice == "5":
        print("Logging out...")
        time.sleep(1)
        menu()
    
    else:
        print("Invalid Command")

def admin_menu():
    admin = Admin()
    while True:
        print("Which feature would you like to use:")
        print("1. Add Product\n" \
        "2. Remove Product\n" \
        "3. Check Users\n" \
        "4. Logout")
        choice = input("Enter your choice : ")

        if choice == "1":
            admin.add_product()
            time.sleep(1)

        elif choice == "2":
            admin.remove_product()
            time.sleep(1)

        elif choice == "3":
            admin.check_users()
            time.sleep(1)

        elif choice == "4":
            print("Logging out...")
            time.sleep(1)
            menu()

        else:
            print("Invalid Command")  


