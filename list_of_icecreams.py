

from icecreamsclass import Icecream


class Creamlist():
    name =  ['vanilla', 'strawberry' , 'chocolate']
    vanilla_cream = [100, 0, 0]
    strawb_cream =   [0, 35, 0]
    chocolate_cream = [0 , 60 , 5]
    cost =  [250,150, 100] 

    def __init__(self) :
      self.creamlist =  []
      self.creamlist.append(Icecream(name = self.name[0], vanilla_cream= self.vanilla_cream[0], strawb_cream = self.strawb_cream[0], choc_cream = self.chocolate_cream[0], cost = self.cost[0]))
      self.creamlist.append(Icecream(name = self.name[1], vanilla_cream= self.vanilla_cream[1], strawb_cream = self.strawb_cream[1], choc_cream = self.chocolate_cream[1], cost = self.cost[1]))
      self.creamlist.append(Icecream(name = self.name[2], vanilla_cream= self.vanilla_cream[2], strawb_cream = self.strawb_cream[2], choc_cream = self.chocolate_cream[2], cost = self.cost[2]))

         

    def get_list_of_creams(self):
        options =  ''

        for index , cream in enumerate(self.creamlist):
            options += f" \n({index}) :  {cream.name} " 
        return options
   
    # def validate_icecream_choice(self, order_name):
    #      order_name = order_name.capitalize()
    #      selfie = self.get_list_of_creams()
    #      slice = selfie.split(',')
    #      if order_name in slice:
    #         return True
    #      return False

    def get_ice_cream_choice(self,order):
     for cream in self.creamlist:
       if cream.name != order:
         continue
       elif cream.name == order:
        return cream
 
        
   