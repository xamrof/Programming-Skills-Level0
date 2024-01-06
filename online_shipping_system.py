# 4. Create an online shipping system with the following features:
# * 		The system has a login that locks after the third failed attempt.
# * 		Display a menu that allows: Sending a package, exiting the system.
# * 		To send a package, sender and recipient details are required.
# * 		The system assigns a random package number to each sent package.
# * 		The system calculates the shipping price. $2 per kg.
# * 		The user must input the total weight of their package, and the system should display the amount to pay.
# * 		The system should ask if the user wants to perform another operation. If the answer is yes, it should return to the main menu. If it's no, it should close the system.

import os
import time
import random

users = [{
    "username": "admin",
    "password": "123456",
    "balance": 2000,
}]


def clear():
    return os.system("cls" if os.name == "nt" else "clear")



def login(username, password):
    for user in users:
        if user["username"] == username and user["password"] == password:
            return True
    return False

def main():
    clear()
    options = ['Sending a package', 'exit']
    while True:
        clear()
        attempts = 0
        username = input("Enter username: ")
        password = input("Enter password: ")
        if login(username, password):
            print("Login successful")
            break
        else:
            print("Login failed")
            attempts += 1
            if attempts == 3:
                print("System locked")
                break
    while True:
        clear()
        print("Welcome,", username)
        for i, option in enumerate(options):
            print(f"{i+1}. {option}")
        choice = input("Enter your choice: ")
        if choice == "1":
            sender = input("Enter sender name: ")
            recipient = input("Enter recipient name: ")
            weight = int(input("Enter weight of package: "))
            price = weight * 2
            print("Package sent successfully")
            print("Package number:", random.randint(1000, 9999))
            print(f"Price to pay: {price}$", )
            another_operation = input("Do you want to perform another operation (y/n): ")
            if another_operation == "y":
                clear()
                continue    
            elif another_operation == "n":
                print("Thank you for using the online shipping system!")
                time.sleep(1)
                break
            time.sleep(2)
        if choice == "2":
            print("Thank you for using the online shipping system!")
            time.sleep(1)
            break
        
    

if __name__ == "__main__":
    main()