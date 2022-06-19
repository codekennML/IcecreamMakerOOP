
class IceCreamMachine():

    def __init__(self):
        self.resources = {'vanilla' : 1000 , 'strawberry' : 1000, 'chocolate' : 1000}

    def is_cream_sufficient(self, icecream):
        """Returns True when icecream can be made, False if resources are insufficient."""
        can_make = True
        for item in icecream.minimum_cream_in_ml:
            if icecream.minimum_cream_in_ml[item] > self.resources[item]:
                print(f"Sorry there is not enough {item} .")
                can_make = False
            return can_make

    def make_icecream(self, order):
        """Deducts the required ingredients from the resources."""
        for item in order.minimum_cream_in_ml:
            self.resources[item] -= order.minimum_cream_in_ml[item]
    
        print("Here is your {} Flavoured Icecream ☕. Enjoy!".format(order.name))
        
        
         
    def report(self):
        """Prints a report of all available resources."""
        print(f"Vanilla Cream : {self.resources['vanilla']}ml")
        print(f"Strawberry Cream: {self.resources['strawberry']}ml")
        print(f"Chocolate Cream: {self.resources['chocolate']}ml")
    

