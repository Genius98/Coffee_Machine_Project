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
profit = 0 # to hold the amount of money & machine has empty money in beggining
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


#Check resources sufficient? When the user chooses a drink, the program should check if there are enough resources to make that drink.
# user's current choice ingredient dictionary will be passed over to order ingredients as a input
def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
             print(f"Sorry there is not enough {item}.")
             return False
    return True


#5. Process coins.If there are sufficient resources to make the drink selected, then the program should prompt the user to insert coins.

def process_coins():
    """Return the total calculated from coins inserted"""
    print (" Please insert coins ")
    # total is the variable that we keep track on & we are gonna return as the output of this func
    total = int(input("How many quarters?: ")) * 0.25 # formula of quarters with dollar
    total += int(input("How many dimes?: ")) * 0.1 # += for added with current quarters
    total = int(input("How many nickles?: ")) * 0.05
    total = int(input("How many pennies?: ")) * 0.01
    return total

#Check transaction successful? Check that the user has inserted enough money to purchase the drink they selected.
def is_transaction_successful(money_received, drink_cost):
        """Return True when the payment is accepted, or False if money is insufficient."""
        if money_received >= drink_cost:
            change = round(money_received - drink_cost, 2)
            print(f"Here is ${change} in change.")
            global profit
            profit += drink_cost #initially profit is zero
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            return False


#Make Coffee

def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item] #look inside the resources for that particular item & we are gonna subtract the amount thts in the order_ingredients
    print(f"Here is your {drink_name} ☕️. Enjoy!")



#step1:  Prompt user by asking “What would you like? (espresso/latte/cappuccino):Check the user’s input to decide what to do next.
is_on = True
#while is_on is true thn keep asking this prompt
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":     #for maintenance guy bcz after getting the choice from user ask prompt should be off
         is_on = False
    elif choice == "report": # report gonna print all the value of the resources
        print(f"Water: {resources['water']}ml")
        print(f"Milk: 5{resources['milk']}ml")
        print(f"Coffee:{resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):  #order_ingredient will be from the drink & hold the values under the key ingredient
            payment = process_coins()  #coins will be saved in payments
            if is_transaction_successful(payment, drink["cost"] ): #money_recieved is basically the payment tht is calculated by coins
                make_coffee(choice, drink["ingredients"]) #drink name is the choice given by user