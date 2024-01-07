# 3. Create an university enrollment system with the following characteristics:
# * 		The system has a login with a username and password.
# * 		Upon logging in, a menu displays the available programs: Computer Science, Medicine, Marketing, and Arts.
# * 		The user must input their first name, last name, and chosen program.
# * 		Each program has only 5 available slots. The system will store the data of each registered user, and if it exceeds the limit, it should display a message indicating the program is unavailable.
# * 		If login information is incorrect three times, the system should be locked.
# * 		The user must choose a campus from three cities: London, Manchester, Liverpool.
# * 		In London, there is 1 slot per program; in Manchester, there are 3 slots per program, and in Liverpool, there is 1 slot per program.
# * 		If the user selects a program at a campus that has no available slots, the system should display the option to enroll in the program at another campus.

import os
import time

users = [{
    "username": "user1",
    "password": "1234"
},
{
    "username": "user2",
    "password": "1234"
},
{
    "username": "user3",
    "password": "1234"
},
{
    "username": "user4",
    "password": "1234"
},
{
    "username": "user5",
    "password": "1234"
},
{
    "username": "user6",
    "password": "1234"
}
]

campus_available = { "London": 1, "Manchester": 3, "Liverpool": 1  }
users_enrolled = []


def clear():
    os.system("cls" if os.name == "nt" else "clear")  

def login(username, password):
    for user in users:
        if user["username"] == username and user["password"] == password:
            return True
    return False

def campus(program):
    name = input("Enter your name: ")
    lastname = input("Enter your lastname: ")
    while True:
        clear()
        print("Please select a campus:")
        for i, city in enumerate(campus_available):
            print(f"{i+1}. {city}")
        choice = input("Enter your choice: ")
        if choice == "1":
            if campus_available["London"] > 0:
                campus_available["London"] -= 1
                print("you have successfully enrolled in the campus London")
                users_enrolled.append({ "name": name, "lastname": lastname, "program": program, "campus": "London" })
                time.sleep(1)
                break
            else:
                print("The campus London is unavailable at this time. chose another")
        if choice == "2":
            if campus_available["Manchester"] > 0:
                campus_available["Manchester"] -= 1
                print("you have successfully enrolled in the campus Manchester")
                users_enrolled.append({ "name": name, "lastname": lastname, "program": program, "campus": "Manchester" })
                time.sleep(1)
                break
            else:
                print("The campus Manchester is unavailable at this time. chose another")
        if choice == "3":
            if campus_available["Liverpool"] > 0:
                campus_available["Liverpool"] -= 1
                print("you have successfully enrolled in the campus Liverpool")
                users_enrolled.append({ "name": name, "lastname": lastname, "program": program, "campus": "Liverpool" })
                time.sleep(1)
                break
            else:
                print("The campus Liverpool is unavailable at this time. chose another")


def main():
    Available_programs = {"Computer Science": 5, "Medicine": 5, "Marketing": 5, "Arts": 5}
    while True:
        login_options = ["Login", "Exit"]
        clear()
        print("Please select an option:")
        for i, option in enumerate(login_options):
            print(f"{i+1}. {option}")
        choice = input("Enter your choice: ")
        login_attempts = 0
        if choice == "1":
            clear()
            while True:
                print("Please enter your username and password:")
                username = input("Enter your username: ")
                password = input("Enter your password: ")
                if login(username, password):
                    print("Login successful!")
                    time.sleep(2)
                    clear()
                    break
                else:
                    clear()
                    print("Invalid username or password. Please try again.")
                    if login_attempts < 3:
                        print(f"You have {3 - login_attempts} attempts left.")
                        login_attempts += 1
                        time.sleep(1)
                    elif login_attempts == 3:
                        print("Your account has been locked. Please try again later.")
                        break
        if choice == "2":
            clear()
            print("Exiting...")
            time.sleep(2)
            break
        print("Welcome,", username)
        while True:
            clear()
            print("Please select a program:")
            for i, program in enumerate(Available_programs):
                print(f"{i+1}. {program}")
            choice = input("Enter your choice: ")
            if choice == "1":
                if Available_programs["Computer Science"] > 0:
                    clear()
                    Available_programs["Computer Science"] -= 1
                    print("You have successfully enrolled in Computer Science.")
                    campus("Computer Science")
                    break
                else:
                    clear()
                    print("Computer Science is unavailable at this time.")
            elif choice == "2":
                if Available_programs["Medicine"] > 0:
                    clear()
                    Available_programs["Medicine"] -= 1
                    print("You have successfully enrolled in Medicine.")
                    campus("Medicine")
                    break
                else:
                    clear()
                    print("Medicine is unavailable at this time.")
            elif choice == "3":
                if Available_programs["Marketing"] > 0:
                    clear()
                    Available_programs["Marketing"] -= 1
                    print("You have successfully enrolled in Marketing.")
                    campus("Marketing")
                    break
                else:
                    clear()
                    print("Marketing is unavailable at this time.")
            elif choice == "4":
                if Available_programs["Arts"] > 0:
                    Available_programs["Arts"] -= 1
                    print("You have successfully enrolled in Arts.")
                    campus("Arts")
                    break
                else:
                    clear()
                    print("Arts is unavailable at this time.")
            else:
                clear()
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()