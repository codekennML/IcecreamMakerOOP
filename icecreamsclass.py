class Icecream():

    def __init__(self, name , cost, vanilla_cream, strawb_cream, choc_cream):
        self.name =  name 
        self.cost = cost
        self.minimum_cream_in_ml = { 
            "vanilla": vanilla_cream,
            "strawberry": strawb_cream,
            "chocolate": choc_cream
        }
 
     
    def get_cost(self):
        return self.cost
    

