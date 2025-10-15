name= input("Enter your name: ")
print("Hello" , name)

age=input("Enter your age: ")
print(type(age))

agenumber=int(age)
print("Next year, you will be:", agenumber+1)
print(type(agenumber))

height= float(input("Enter your height in meters: "))
print("You are" , height, "meters tall.")
print(type(height))

#Challenge 1: Favorite Color

color=input("Enter your favorite color: ")
print("Your Favorite Color is: ", color)

#Challenge 2

numberone = int(input("Pick any number: "))
numbertwo = int(input("Pick another number: "))
print(numberone + numbertwo)


#Challenge 3

import math

diameter = int(input("Pick a diameter for a circle: "))
print((diameter / 2) ** 2 * math.pi)

#Challenge 4
import random
Die = int(input("How many sides would you like the die to have? :"))
print(random.randint(1,Die))


