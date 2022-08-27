coffee_types = {
        "espresso" : {
            "ingredients":{
                "water"  : 50,
                "coffee" : 18,
                },
                "cost":50,
        },    
    
         "latte" : {
            "ingredients":{
                "water"  : 200,
                "coffee" : 24,
                "milk" : 150,
                },
                "cost":150,
        },        
         
        "cappuccino":{
            "ingredients" :{
                "water" :50,
                "coffee" :24,
                "milk" :100,
                },
                "cost": 250
        }        
}
#print(coffee_types)

profit = 0
resources = {
    "water":300,
    "milk" : 200,
    "coffee":100,
}
#print(resourses)

def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry, there is not enough {item}.") 
            return False
    return True   

def process_coin():
    """Returns the total calculated of inserted coins"""
    print("Please insert coins.")
    total = int(input("How many 5 rupee coins?: ")) * 5   
    total += int(input("How many 10 rupee coins?: ")) * 10  
    total += int(input("How many 20 rupee coins?: ")) * 20
    return total   

def is_transaction_successful(money_recieved, drink_cost):
    """RETURN TRUE WHEN THE PAYMENT IS ACCEPTED,OR FALSE IF MONEY IS INSUFFICIENT"""
    if money_recieved >= drink_cost:
        change = round(money_recieved - drink_cost,2)
        print(f"Here is Rs{change} in change.")
        global profit
        profit += drink_cost 
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False    

def make_coffee(drink_name,order_ingredients):
    """DEDUCT THE REQUIRED INGREDIENTS FROM THE RESOURCES"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕.")


machine_should_continue = True
while machine_should_continue:
    customer_choice = input("What would you like? (espresso/latte/cappuccino): ")
    if customer_choice == "off":
        machine_should_continue = False
    elif customer_choice == "report":
        water = resources['water']
        milk  = resources['milk']
        coffee = resources['coffee']
        print(f"water : {water} \nmilk : {milk} \ncoffee : {coffee} \nmoney : {profit}")  

    else: 
        drink = coffee_types[customer_choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coin()
            if is_transaction_successful(payment,drink["cost"]):
                make_coffee(customer_choice,drink["ingredients"])

    
    



        

