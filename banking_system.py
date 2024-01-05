# 1. Create an online banking system with the following features:

# * Users must be able to log in with a username and password.
# * If the user enters the wrong credentials three times, the system must lock them out.
# * The initial balance in the bank account is $2000.
# * The system must allow users to deposit, withdraw, view, and transfer money.
# * The system must display a menu for users to perform transactions. 

import os
import time

users = [{
    "username": "admin",
    "password": "123456",
    "balance": 2000,
}]

def register(username, password):
    users.append({
        "username": username,
        "password": password,
        "balance": 2000,
    })


def login(username, password):
    for user in users:
        if user["username"] == username and user["password"] == password:
            return True
    return False
    
def deposit(amount, username):
    user = next(user for user in users if user["username"] == username)
    if amount < 0:
        return "Invalid amount"
    user["balance"] += amount
    return user["balance"]

def withdraw(amount, username):
    user = next(user for user in users if user["username"] == username)
    if amount < 0:
        return "Invalid amount"
    if amount > user["balance"]:
        return "Insufficient funds"
    user["balance"] -= amount
    return user["balance"]

def view_balance(username):
    user = next(user for user in users if user["username"] == username)
    return user["balance"]

def transfer(amount, username, recipient):
    user = next(user for user in users if user["username"] == username)
    recipient = next(user for user in users if user["username"] == recipient)
    if amount < 0:
        return "Invalid amount"
    if amount > user["balance"]:
        return "Insufficient funds"
    user["balance"] -= amount
    recipient["balance"] += amount
    return user["balance"]

def clear():
    return os.system("cls" if os.name == "nt" else "clear")

def main():
    options = ["Login", "Register", "exit"]
    menu_options = ["View Balance", "Deposit", "Withdraw", "Transfer", "exit"]

    print("Welcome to the online banking system!")
    while True:
        clear()
        print("Please select an option:")
        for i, option in enumerate(options):
            print(f"{i+1}. {option}")
        choice = input("Enter your choice: ")
        if choice == "1":
            clear()
            count = 0
            while True:
                print("Please enter your username and password:")
                username = input("Enter your username: ")
                password = input("Enter your password: ")
                if login(username, password):
                    print("Login successful!")
                    break
                else:
                    if count == 3:
                        print("Too many failed attempts. Account locked.")
                        break
                    print("Invalid username or password. Please try again.")
                    count += 1
            print("Welcome,", username)
            while True:
                clear()
                print("Please select an option:")
                for i, option in enumerate(menu_options):
                    print(f"{i+1}. {option}")
                choice = input("Enter your choice: ")
                if choice == "1":
                    print("Your balance is:", view_balance(username))
                    time.sleep(2)
                elif choice == "2":
                    amount = float(input("Enter the amount to deposit: "))
                    deposit(amount, username)
                    print("Amount is added successfully")
                    time.sleep(2)
                elif choice == "3":
                    amount = float(input("Enter the amount to withdraw: "))
                    withdraw(amount, username)
                    print("Amount is withdraw successfully")
                    time.sleep(2)
                elif choice == "4":
                    amount = float(input("Enter the amount to transfer: "))
                    recipient = input("Enter the recipient's username: ")
                    print("Your balance is:", transfer(amount, username ,recipient))
                    time.sleep(2)
                elif choice == "5":
                    print("Thank you for using the online banking system!")                    
                    time.sleep(1)
                    os.system("cls" if os.name == "nt" else "clear")
                    break
                else:
                    print("Invalid choice. Please try again.")
                    time.sleep(1)
                    continue               
        elif choice == "2":
            clear()
            username = input("Enter a username: ")
            password = input("Enter a password: ")
            register(username, password)
            print("Registration successful!")
        elif choice == "3":
            clear()
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

