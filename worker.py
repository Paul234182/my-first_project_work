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

# object orientated programming

class dog:
    def bark(self):
        print("bark")
    def add_value(self, x):
        return x +1

     
# it is an instant of the class dog          
d= dog()
print(type(d))
d.bark()
print(d.bark())
d.add_value(6)
print(d.add_value(6))

class dog2:
    def __init__(self, name, age):
        self.name= name
        self.age= age
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def set_age(self, age):
        self.age= age
    def set_name(self, name):
        self.name = name
       
d1= dog2("billie", 25)
d1.set_age(20)
print(d1.set_age(20))
print(d1.get_age())
d2= dog2("tom", 35)
d2.set_name('Chika')
print(d2.set_name('Chika'))
print(d2. get_age())

class student:
    def __init__(self, name, age, grade):
        self.name= name
        self.age= age
        self.grade= grade
    def get_grade(self):
        return self.grade

class course:
    def __init__(self, name, max_students):
        self.name= name
        self.max_students= max_students
        self.students= []
    def add_students(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False
    def get_average_grade(self):
        value= 0
        for student in self.students:
            value += student.get_grade()
        return value/ len(self.students)
    
        
        

s1= student('Chika', 35, 60)
s2= student('Peter', 27, 58)
s3= student('Paul', 36, 98)


# adding students records in the course
courses= course('Art', 2)
courses.add_students(s1)
courses.add_students(s2)
courses.add_students(s3)
print(courses.students[0].name)
print(courses.get_average_grade())
print(courses.add_students(s3))

# inheritance
class pet:
    def __init__(self, name, age):
        self.name = name
        self.age= age
    def display(self):
        print(f"i am {self.name} and i am {self.age} years old")
    def speak(self):
        print("i don't have what to say")
        

class cat(pet):
    def __init__(self, name, age):
        self.name = name
        self.age= age
    def speak(self):
        print("meow")
class dog(pet):
    def __init__(self, name, age):
        self.name= name
        self.age= age
    def speak(self):
        print("bark")

p1= pet('Chika', 20)
p2= pet('Tommy', 17)
p3= pet('Frank', 26)

p1.display()
print(p1.display())
p1.speak()
print(p1.speak())

c1= cat('sammy', 15)
c1.display()
c1.speak()
print(c1.speak())

print(c1.display())
d1= dog('chilly', 29)
d1.speak()
print(d1.speak())
d1.display()
print(d1.display())



    




    

    


        




    
      

       
        


    
    





        



                
             

     







        



        






    

    

       
   

  

   

    


   

    
        


    
    
        

   


