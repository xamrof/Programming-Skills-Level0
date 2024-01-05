# 5. Develop a finance management application with the following features:
# * 		The user records their total income.
# * 		There are categories: Medical expenses, household expenses, leisure, savings, and education.
# * 		The user can list their expenses within the categories and get the total for each category.
# * 		The user can obtain the total of their expenses.
# * 		If the user spends the same amount of money they earn, the system should display a message advising the user to reduce expenses in the category where they have spent the most money.
# * 		If the user spends less than they earn, the system displays a congratulatory message on the screen.
# * 		If the user spends more than they earn, the system will display advice to improve the user's financial health.

import os
import time

def clear():
    return os.system("cls" if os.name == "nt" else "clear")


def main():
    expenses = ["Medical expenses", "Household expenses", "Leisure", "savings", "education", "Total", "Exit"]
    Medical_expenses = 0
    Household_expenses = 0
    Leisure = 0
    savings = 0
    education = 0
    clear()
    print("Welcome to the Finance Management System!")
    income = input("Please enter your income: ")
    clear()
    while True:
        print("Please select a category:")
        for i, option in enumerate(expenses):
            print(f"{i+1}. {option}")
        choice = input("Enter your choice: ")
        if choice == "1":
            clear()
            print("Please enter your expenses for Medical expenses:")
            Medical_expenses += float(input("Enter your expenses: "))
            clear()
        if choice == "2":
            clear()
            print("Please enter your expenses for Household expenses:")
            Household_expenses += float(input("Enter your expenses: "))
            clear()
        if choice == "3":
            clear()
            print("Please enter your expenses for Leisure:")
            Leisure += float(input("Enter your expenses: "))
            clear()
        if choice == "4":
            clear()
            print("Please enter your expenses for savings:")
            savings += float(input("Enter your expenses: "))
            clear()
        if choice == "5":
            clear()
            print("Please enter your expenses for education:")
            education += float(input("Enter your expenses: "))
            clear()
        if choice == "6":
            clear()
            print("Expenses:")
            print(f"Medical expenses: {Medical_expenses}")
            print(f"Household expenses: {Household_expenses}")
            print(f"Leisure: {Leisure}")
            print(f"savings: {savings}")
            print(f"education: {education}")
            print(f"Total: {Medical_expenses + Household_expenses + Leisure + savings + education}")
            if float(income) > (Medical_expenses + Household_expenses + Leisure + savings + education):
                print("Congratulations! You have saved money!")
                time.sleep(2)
            elif float(income) < (Medical_expenses + Household_expenses + Leisure + savings + education):
                print("You have spent more than you earned. Please consider reducing your expenses.")
                time.sleep(2)
            elif float(income) == (Medical_expenses + Household_expenses + Leisure + savings + education):
                print("You have spent the same amount of money you earned. Please consider reducing your expenses.")
                time.sleep(2)
            input("Press enter to exit...")
            clear()
            break
        if choice == "7":
            clear()
            print("Exiting...")
            time.sleep(2)
            clear()
            break


if __name__ == "__main__":
    main()