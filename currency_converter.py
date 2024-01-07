# 2. Create a currency converter between CLP, ARS, USD, EUR, TRY, GBP with the following features:
# * 		The user must choose their initial currency and the currency they want to exchange to.
# * 		The user can choose whether or not to withdraw their funds. If they choose not to withdraw, it should return to the main menu.
# * 		If the user decides to withdraw the funds, the system will charge a 1% commission.
# * 		Set a minimum and maximum amount for each currency, it can be of your choice.
# * 		The system should ask the user if they want to perform another operation. If they choose to do so, it should restart the process; otherwise, the system should close.

#TODO: ARREGLAR

menu = {
    "CLP": {'min': 1000, 'max': 5000, 'change': 0.00112},
    "ARS": {'min': 2000, 'max': 3000, 'change': 0.00123162},
    "USD": {'min': 10, 'max': 10000, 'change': 1},
    "EUR": {'min': 10, 'max': 10000, 'change': 1.0940},
    "TRY": {'min': 5000, 'max': 5000, 'change': 1.6769 },
    "GBP": {'min': 2000, 'max': 4000, 'change': 1.27190},
    }

def main():
    while True:
        print("Welcome to the currency converter!")
        for i, currency in enumerate(menu.keys()):
            print(currency)
        print("Enter Exit to exit the program")
        currency = input("Enter your currency: ")
        if currency.lower() == "exit":
            break
        currency_to_convert = input("Enter the currency you want to convert to: ")
        amount = float(input("Enter the amount: "))
        if currency_to_convert in menu.keys():
            if menu[currency_to_convert]['min'] <= amount <= menu[currency_to_convert]['max']:
                converted_amount = amount - (amount * 0.01)
                print(f"The converted amount is {amount * 0.01}")
                print("Do you want to withdraw your funds?")
                choice = input("Enter Yes or No: ")
                if choice.lower() == "yes":
                    change = converted_amount * menu[currency]['change']
                    currency_converted = change * menu[currency_to_convert]['change']
                    print(f"The amount {currency_converted} has been withdrawn")
                    print("Thank you for using the currency converter!")
                    another_operation = input('do you want another operation?')
                    if another_operation.lower() == "yes":
                        continue
                    else:
                        print("Thank you for using the currency converter!")
                        break
                elif choice.lower() == "no":
                    continue
                    
            else:
                print("The amount is not within the allowed range")
        

if __name__ == "__main__":
   main()