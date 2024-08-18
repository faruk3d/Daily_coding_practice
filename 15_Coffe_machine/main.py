MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def check_resources():
    if resources['water'] < MENU[user_choice]['ingredients']['water']:
        print('sorry')
        user_choice
    elif resources['milk'] < MENU[user_choice]['ingredients']['milk']:
        print('sorry')
        user_choice
    elif resources['coffee'] < MENU[user_choice]['ingredients']['coffee']:
        print('sorry')
        user_choice

bank = []

report = f"water: {resources['water']}\n milk : {resources['milk']}\n coffee : {resources['coffee']}\n money : {bank} €"
# TODO 1. “What would you like? (espresso/latte/cappuccino):”


coffee_list = ["espresso", "latte", "cappuccino"]
user_choice = input(str("What would you like? (espresso / latte / cappuccino):\n"))
if user_choice in coffee_list:
    print(f"Espresso : {MENU['espresso']['cost']} €, Latte : {MENU['latte']['cost']} €, Cappuccino : {MENU['cappuccino']['cost']} €. Please insert coins.")
    check_resources()
    cent_50 = input("how many 50 cent? ")
    cent_20 = input("how many 20 cent? ")
    cent_10 = input("how many 10 cent? ")
    user_coins = int(cent_50) * 0.5 + int(cent_20) * 0.2 + int(cent_10) * 0.1
    bank.append(user_coins)
    resources.update(water =  resources['water'] - MENU[user_choice]['ingredients']['water'], milk = resources['milk'] - MENU[user_choice]['ingredients']['milk'], coffee = resources['coffee'] - MENU[user_choice]['ingredients']['coffee'])
    print(resources)

elif user_choice == "report":
    print(report)
else:
    print("Wrong input, DUDE")


# TODO 2. Turn off the Coffee Machine by entering “off” to the prompt
# TODO 3. Print report
# TODO 4. Check resources sufficient
# TODO 5. Process coins
# TODO 6. Check transaction successful
# TODO 7. Make coffe

