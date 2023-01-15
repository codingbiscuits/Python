import math

OPTIONS = ["espresso", "latte", "cappuccino", "off", "report"]

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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


def check_resources(ingredients):
    for item in ingredients:
        if ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
        else:
            return True


def check_payment(cost, pay):
    if pay == cost or pay >= cost:
        refund = round(pay - cost, 2)
        print(f"Payment successful. Your refund is: ${refund}.")
    else:
        print("Not enough coins inserted. Please try again with more coins.")


def deduct_resources(ingredients, resources):
    for item in ingredients:
        resources[item] -= ingredients[item]


profit = 0.00
is_power_on = True
while is_power_on:
    choice = ""
    while choice not in OPTIONS:
        choice = input(
            "What would you like? (espresso/latte/cappuccino): ").lower()

    if choice == "off":
        is_power_on = False

    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: {profit}")

    else:
        ingredients = MENU[choice]["ingredients"]
        enough_resources = check_resources(ingredients)
        if enough_resources:
            cost = round(MENU[choice]["cost"], 2)
            print(f"Your {choice} will cost ${cost}0.")

            wrong_input = True
            while wrong_input:
                try:
                    quarters = int(
                        input("How many quarters would you like to use? "))
                    quarter_amt = quarters * 0.25
                    dimes = int(
                        input("How many dimes would you like to use? "))
                    dime_amt = dimes * 0.10
                    nickels = int(
                        input("How many nickels would you like to use? "))
                    nickel_amt = nickels * 0.05
                    pennies = int(
                        input("How many pennies would you like to use? "))
                    penny_amt = pennies * .01
                    wrong_input = False
                except:
                    print("Error: You must type a number..")

            total_amt = round(quarter_amt + dime_amt +
                              nickel_amt + penny_amt, 2)
            print(f"Your total payment is: ${total_amt}.")

            refund = check_payment(cost, total_amt)
            profit += cost

            deduct_resources(ingredients, resources)

        else:
            choice = ""
