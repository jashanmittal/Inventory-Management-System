# Inventory Management System

A command-line inventory and shop management system with separate customer and admin roles. Customers can register, browse products, make purchases, track their inventory, and manage their account balance. Admins can manage stock, monitor users, and view all transactions across the platform.

## Features

**Customer:**
- Register and login with unique account number
- Browse and purchase products
- Check account balance and add funds
- View personal inventory of purchased items
- View transaction history

**Admin:**
- Secure admin login
- Add and remove products from stock
- View all registered users and their balances
- Low stock notifications
- View transaction history across all accounts

## How to Run
main.py

## Data Persistence
Account and stock data is saved using JSON, so all information persists between sessions.

## What I Learned
- Multi-role system design (Customer vs Admin)
- Object serialization using `__dict__` and unpacking with `**kwargs`
- Handling nested data structures in JSON
- Managing relationships between multiple object types (accounts, products, transactions)
- Proper exception handling for invalid input and corrupted/missing save files

## Future Improvements
- Add product categories
- Implement discount/coupon system
- Add order history with timestamps for purchases specifically