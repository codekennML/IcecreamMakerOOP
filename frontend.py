from icecream import IceCreamMachine
from list_of_icecreams import Creamlist

creams =  Creamlist()
machine =  IceCreamMachine()
is_on = True

def welcome():
    print('''
             )))
            (((
          +-----+
          |     |] - Welcome to CodeKennML Icecream Spot!
          `-----' 
    
          ------ MENU ------ 
            Vanilla Flavoured Icecream (N200)
            Strawberry Flavoured Icecream (N150)
            Chocolate Flavoured Icecream (N100)
          ------------------
    
          PS: Type "report" at any moment
          to check our available resources.
          Type "off" to end 
        ''')

while is_on:
    # welcome()
    options = creams.get_list_of_creams()
    user_choice = str(input(f'What flavour of our amazing icecream would you like?\nOptions ({options}): ')).strip().lower()
    if user_choice == 'off':
        print('<< Transaction  Ended>>')
        is_on = False
    elif user_choice == 'report':
            machine.report()
            continue
    elif creams.get_ice_cream_choice(user_choice) is None:
        print('Error. Please choose an available option.')
    else:
        beverage = creams.get_ice_cream_choice(user_choice) 
        sufficient_resources = machine.is_cream_sufficient(beverage) #True/False 
        if sufficient_resources :
            print('Done! Allow us to make your beverage now.')
            machine.make_icecream(beverage) 
            is_on = False


