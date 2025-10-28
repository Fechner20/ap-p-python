#LOOPS IN PYTHON
#Loops repaeat a block of code until they hit a limit or condition.
#They exist to save us from typing th esame line 500 times.
#Python gives us for-loops and while-loops. 

import time


animals=["lamb", "sheep", "cow", "goose", "donkey"]
animals[0]

print("Our Animals:", animals)

print("----For Loop: visiting each animal----")
for animal in animals:
    print("Now Petting a", animal)
    time.sleep(0)
   
    if animal == "lamb":
         print("Hi lamb!")

print("\nI have pet all the animals.")

if animal == "sheep":
    print("Hi Sheep!")

#range
for num in range(2,11,3):
        print("Even number: ", num,)


print("---Iterating over strings --\n")

fav_word="loquacious"
letter_list= []

for letter in fav_word:
    print(letter, end= "")
    letter_list.append(letter)
    print(letter_list)

print()


# -------------------------------------------------------------------------------------------------------
# WHILE LOOPS
# -------------------------------------------------------------------------------------------------------


#+= to add a variable, -= to subtract a variable
import time
count=0

while count < 5:
     print(f"Looping' . We are on loop # {count}. ")
     count += 1 
     time.sleep(0.5)

print ("We have escaped the loop")

user_input = ""

 
while user_input != "exit":
   user_input=input(" Type exit to escape:")



count2 = 60
increment = 1

while count2 > 0:
     count2 -= increment
     increment += 1

     if count2<0:
        break

     print(count2)

    

    # CHALLENGE 1
import random

amount=int(input("How many different fruits should I buy at the grocery store out of the the 7 they have?: "))
fruits=["Blackberrys", "Bananas", "Jackfruit", "Dragon","Apples", "Bluberrys", "Mangos"]

for fruit in range(amount):
     print("You picked: ",random.choice(fruits))



# CHALLENGE 2

     