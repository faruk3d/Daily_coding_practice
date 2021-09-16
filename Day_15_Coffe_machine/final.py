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

money = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_res_suff(order_ingr):
    """return True when order can be made, False if ingredients are insuffiient"""
    is_enough = True
    for item in order_ingr:
        if order_ingr[item] >= resources[item]:
            print(f"Sorry, there is not enough {item}.")
            is_enough = False
    return is_enough


def insert_money():
    """returns the total calculated from coins inserted"""
    print("Please insert coins.")
    total_coins = int(input("how many quarters?: ")) * 0.25
    total_coins += int(input("how many dimes?: ")) * 0.1
    total_coins += int(input("how many nickles?: ")) * 0.05
    total_coins += int(input("how many pennies?: ")) * 0.01
    return total_coins



def if_transaction_successful(money_recieved, drink_cost):
    """return True when the payment is accepted, or False is money is insufficient"""
    trans_succ = True
    if money_recieved >= drink_cost:
        change = round(money_recieved - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global money
        money += drink_cost
        return trans_succ
    else:
        print("Sorry, that's not enough money, Money refunded.")
        trans_succ = False        


def make_coffee(drink_name, order_ingr):
    """deduct the required ingredients from the resources."""
    for item in order_ingr:
        resources[item] -= order_ingr[item]
    print(f"Here is your {drink_name}")



is_on = True
while is_on : 
    choice = input("What would you like? (espresso / latte / cappuccino):")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water : {resources['water']} ml")
        print(f"Milk : {resources['milk']} ml")
        print(f"Coffee : {resources['coffee']} g")
        print(f"Money : $ {money}")
    else:
        drink = MENU[choice]
        if is_res_suff(drink["ingredients"]):
            payment = insert_money()
            if if_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
