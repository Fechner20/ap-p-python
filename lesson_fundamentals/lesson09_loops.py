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
print("\nI have pet all the animals.")

if animal == "sheep":
    print("Hi Sheep!")

#range
for num in range(2,11,3):
        print("Even number: ", num,)