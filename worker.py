import pandas as pd
import numpy as np
food_consumption= pd.read_csv('food_consumption.csv')
print(food_consumption)
food_consumption.describe()
print(food_consumption.describe())
print(food_consumption.head())

np.mean(food_consumption['consumption'] > 30)
print(np.mean(food_consumption['consumption'] > 30))

np.median(food_consumption['co2_emission'])
print(np.median(food_consumption['co2_emission']))

food_consumption.loc[food_consumption['co2_emission'] > 35.22]['consumption']
print(food_consumption.loc[food_consumption['co2_emission'] > 35.22]['consumption'])
food_consumption.dtypes
print(food_consumption.dtypes)

MASK1= food_consumption['consumption']>= 3.24
MASK2= food_consumption['country']== 'USA'
food_consumption2= food_consumption[MASK1 & MASK2].sort_values(by= 'consumption', ascending= True)
print(food_consumption2)
food_consumption.groupby('country')['co2_emission'].mean()
print(food_consumption.groupby('country')['co2_emission'].mean())
# Calculate total co2_emission per country: 

food_consumption.groupby('country')['co2_emission'].sum().sort_values( ascending= False)
print(food_consumption.groupby('country')['co2_emission'].sum().sort_values( ascending= False))
# Calculate mean and median consumption in Belgium
be_consumption= np.mean(food_consumption['country']== 'Belgium')
print(be_consumption)
be_consumption= np.median(food_consumption['country']== 'Belgium')
print(be_consumption)

be_consumption= food_consumption.groupby(food_consumption ['country']== 'Belgium')['consumption'].mean()
print(be_consumption)

def consumption():
  results=  food_consumption['co2_emission'].strip().lower()
  return results
print(results)

class gaspoweredcars:
    def __init__(self, make, models, fuel_level):
        self.make= make
        self.models= models
        self.energy_level= fuel_level
    def start(self):
        if self.fuel_level > 0:
            print(f"the {self.make} {self.models} has started successfully")
        else:
            print(f"the {self.make} {self.models} hasn't started successfully")
    def refueled(self):
        if self.fuel_level < 25:
            print(f"refueling {self.make} {self.models} is needed")
            self.fuel_level = 100
        else:
            print(f"the {self.make} {self.models} has been refueled")
 


    def check_energy(self):
        print(f"the {self.make} {self.models} has {self.energy_level}% energy left ")
    
    def repair_cars(self):
            if self.energy_level > 100:
                print(f"the {self.make} {self.models} is in a good condition")
                self.energy_level < 100
            else:
                print(f"the {self.make} {self.models} is not in a good condition")
    

   
class electriccar(gaspoweredcars):
        def __init__(self, make, models, energy_level =100 ):
            super().__init__(make, models, energy_level)
        
            self.make= make
            self.models= models
            self.energy_level= energy_level
            
            
        def start(self):
            if self.energy_level > 0:
                print(f"the {self.make} {self.models} has started")
            else:
                print(f"the {self.make} {self.models} hasn't started")
        
        def recharged(self):
            if self.energy_level < 25:
                print(f"recharging {self.make} {self.models} is needed")
                self.energy_level = 100
            else:
                print(f"the {self.make} {self.models} has been recharged")
        def repair_cars(self):
            if self.energy_level > 100:
                print(f"the {self.make} {self.models} is in a good condition")
                self.energy_level < 100
            else:
                print(f"the {self.make} {self.models} is not in a good condition")
        def calculated_value(self):
            not_class= {self.models} != 'model 2' 
            return not_class
        def check_energy(self):
            if self.energy_level > 100:
                print(f"the {self.make} {self.models} has {self.energy_level}% energy left ")
                self.energy_level< 100
            else:
                print(f"the {self.make} {self.models} has not {self.energy_level}% energy left ")
        



            
    

       
    
electriccar1 = electriccar('Tesla', 'Model 3', 40)
electriccar2 = electriccar('Nissan Leaf', 'Model 5', 25)
electriccar3 = electriccar('Chevrolet Bolt', 'Model 6', 60)
electriccar4 = electriccar('BMW', 'I4', 80)

electriccar1.calculated_value()
print(electriccar1.calculated_value())

electriccar1.start()
print(electriccar1.start())

electriccar1.calculated_value()
print(electriccar1.calculated_value())

electriccar1.check_energy()
print(electriccar1.check_energy())




gaspoweredcars5= gaspoweredcars('Honda', 'civic', 35)
gaspoweredcars6=  gaspoweredcars('Ford', 'mustang', 60)
gaspoweredcars7=  gaspoweredcars('Toyota', 'camry', 58)
gaspoweredcars8=  gaspoweredcars('Jeep', 'wrangler', 65)

electriccar2.repair_cars()
print(electriccar2.repair_cars())

gaspoweredcars5.repair_cars()
print(gaspoweredcars5.repair_cars())





    
      

       
        


    
    





        



                
             

     







        



        






    

    

       
   

  

   

    


   

    
        


    
    
        

   


