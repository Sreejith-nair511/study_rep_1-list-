#IN Python,when we use a variable it actual stores a refernce to the memory location where the values is been stored 
#what this means is in python,references gives us values 
#commonly the two method pass by values and passs by reference 
#for example 
buggati='chiron'
GMC='cadillac'
#what python does is it makes temporary storage by creating a refernce to the value in memory 
#referernce is a value which points towards a piece of data 
#list refernce is a value which points towards a list 
#variable will contail the reference to the value and the exact copy of the value 
#an important thing to keep in mind ,python will create reference for muteable data type only 
#for unmuteable data type,it will directly store data towards it 
print(id('chiron'))#address in memory displayed  
#copy() and deepcopy() function to actually copy the muteable data type
import copy
cars=['subaru','alfa ro','husqverna'] 
elec_cars=copy.copy(cars)
cars[2]='tesla'
print(cars)
print(elec_cars)
#deepcopy() for inner list 
