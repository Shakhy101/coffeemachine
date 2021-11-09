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


def print_report(resources, money):
    for resource in resources:
        ingredient = resource.title()
        ingredient_amount = resources[resource]
        print(f"{ingredient}: {ingredient_amount}")
    print(f"Money: {money}")


def check_resources(user_drink):
    for resource in resources:
        if resources[resource] < MENU[user_drink]["ingredients"][resource]:
            print(f"Sorry there is not enough {resource}")
            return False
    return True


def coffee_machine(user_drink, money):

    if user_drink == "off":
        return False
    elif user_drink == "report":
        print_report(resources, money)
        return True
    else:
        
        return True


def count_coins(quarters, nickles, dimes, pennies):
    total_inserted = 0.25 * quarters + 0.05 * \
        nickles + 0.1 * dimes + 0.01 * pennies
    return round(total_inserted, 2)


def insert_money():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    return count_coins(quarters, nickles, dimes, pennies)


def check_price(inserted_money, drink_price):
    if inserted_money < drink_price:
        print("Sorry, that's not enough money. Money refunded.")
        enough_money = False
        return enough_money
    else:
        change = round(inserted_money - drink_price, 2)
        print(f"Here is ${change} in change")
        enough_money = True
        return enough_money


money = 0
machine_on = True
available_drinks = []
for available_drink in MENU:
    available_drinks.append(available_drink)
while machine_on:
    inserted_money = 0
    user_drink = input(
        "​What would you like? (espresso/latte/cappuccino): ").lower()
    machine_on = coffee_machine(user_drink, money)
    if user_drink in available_drinks:
        if check_resources(user_drink):
            drink_price = MENU[user_drink]["cost"]
            inserted_money = insert_money()
            if check_price(inserted_money, drink_price):
                print(f"Here is your {user_drink}. Enjoy!")
                for resource in resources:
                    resources[resource] = resources[resource] - \
                        MENU[user_drink]["ingredients"][resource]
                money += drink_price
