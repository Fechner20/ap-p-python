#Python libraries are repositories of code you can import into your own code

import math
print("\n--- Math Library ---\n")

print("Square Root: ", math.sqrt(169))
print("Round Up: ", math.ceil(6.7))
print("Round Down:",math.floor(6.7))
print("Power:" , math.pow(3,3))

#------------------
#  RANDOM LIBRARY
#------------------

#PRECURSOR CHALLENGE

Seed=5.106
Step1=Seed*0.7
Step2=Step1-6.7
Step3=Seed+4.1
Step4=math.floor(Step3)
print(Step4)



import random

print("\n--- Random Library ---\n")

print("Random Integer:" , random.randint(4,20))

print(random.random())

mylist=["Green Eggs","Ham"]
print(random.choice(mylist))

random.shuffle(mylist)
print(mylist)


#Challenge 1

radius=14/2
circle_area=radius**2*math.pi
print(circle_area)

#Challenge 2

die_roll=random.randint(1,6)
print(die_roll)


 

