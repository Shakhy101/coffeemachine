MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk" : 0,
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

#TODO: 1. Prompt user by asking “​What would you like? (espresso/latte/cappuccino):​” 
# a. Check the user’s input to decide what to do next.  
# b. The prompt should show every time action has completed, e.g. once the drink is 
# dispensed. The prompt should show again to serve the next customer. 
money = 0

def make_report(money, resources):
    for resource in resources:
        print(f"{resource.title()}: {resources[resource]}")
    print(f"Money: {money}")


def insert_money():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    return count_coins(quarters, nickles, dimes, pennies)
    
# def make_espresso():
#     insert_money()

def count_coins(quarters, nickles, dimes, pennies):
    total_inserted = 0.25 * quarters + 0.05 * nickles + 0.1 * dimes + 0.01 * pennies
    return total_inserted


def check_price(inserted_money, drink_price):
    if inserted_money < drink_price:
        print("Sorry, that's not enough money. Money refunded.")
        enough_money = False
        return enough_money
    else:
        change = inserted_money - drink_price
        print(f"Here is ${change} in change")
        enough_money = True
        return enough_money
        
def make_coffee(drink, resources, money):
    # check if there are resources to make chosen drink. If not, write what is missing and return to prompt
    
    for resource in resources:
        print(MENU[drink]["ingredients"][resource]) 
        if MENU[drink]["ingredients"][resource] >= resources[resource]:
            return f"There is not enough {resource}"
    # process coins
    inserted_money = insert_money()
    drink_price = MENU[drink]["cost"]
    print(f"price: {drink_price}")
    print(inserted_money)
    if check_price(inserted_money, drink_price):
        print(f"Here is your {drink}. Enjoy!")
        for resource in resources:
            resources[resource] = resources[resource] - MENU[drink]["ingredients"][resource]
        money += drink_price 
    ## prompt insert coins
    ##calculate coins
    

def coffee_machine():
    
    drink = input("​What would you like? (espresso/latte/cappuccino): ").lower()

    if drink == "espresso" or drink == "latte" or drink == "cappuccino":
        make_coffee(drink, resources, money)
        return True
    elif drink == "report":
        make_report(money, resources)
        return True
    elif drink == "off":
        return False      
    else:
        print("That's not a button, try again. ")
        return True


machine_on = True
while machine_on:
    machine_on = coffee_machine()

# print(MENU["espresso"]["ingredients"])


    
    

# TODO: 2. Turn off the Coffee Machine by entering “​off​” to the prompt. 
# a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off 
# the machine. Your code should end execution when this happens.

# TODO: 3. Print report. 
# a. When the user enters “report” to the prompt, a report should be generated that shows 
# the current resource values. e.g.  
# Water: 100ml 
# Milk: 50ml 
# Coffee: 76g 
# Money: $2.5

# TODO: 4. Check resources sufficient? 
# a. When the user chooses a drink, the program should check if there are enough 
# resources to make that drink.  
# b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should 
# not continue to make the drink but print: “​Sorry there is not enough water.​” 
# c. The same should happen if another resource is depleted, e.g. milk or coffee.

# TODO: 5. Process coins. 
# a. If there are sufficient resources to make the drink selected, then the program should 
# prompt the user to insert coins.  
# b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01 
# c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2 
# pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52

# TODO: 6. Check transaction successful? 
# a. Check that the user has inserted enough money to purchase the drink they selected. 
# E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the 
# program should say “​Sorry that's not enough money. Money refunded.​”. 
# b. But if the user has inserted enough money, then the cost of the drink gets added to the 
# machine as the profit and this will be reflected the next time “report” is triggered. E.g.  
# Water: 100ml 
# Milk: 50ml 
# Coffee: 76g 
# Money: $2.5 
# c. If the user has inserted too much money, the machine should offer change.  
# E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal 
# places.

# TODO: 7. Make Coffee. 
# a. If the transaction is successful and there are enough resources to make the drink the 
# user selected, then the ingredients to make the drink should be deducted from the 
# coffee machine resources.  
 
# E.g. report before purchasing latte: 
# Water: 300ml 
# Milk: 200ml 
# Coffee: 100g 
# Money: $0 
 
# Report after purchasing latte: 
# Water: 100ml 
# Milk: 50ml 
# Coffee: 76g 
# Money: $2.5 
 
# b. Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If 
# latte was their choice of drink.