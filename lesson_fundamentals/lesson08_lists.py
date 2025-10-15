#LISTS IN PYTHON
#Lists store multiple values in one variable.
#They are ordered,mutable (changeable), and allow duplicates

print()
print("---Lists in Python---")


animals=["Koala","Rat", "Blobfish"]
numbers=[1,2,3,4]
mixed=["James",20,False,20.20]

print(animals)
print(numbers)
print(mixed)

print("First Element: ", animals[0])
print("Second Element: ",animals[1])
print("Last element: ", animals[-1])



#Modify Lists

animals[0] is "babirusa"
print(animals)

animals.append("glass frog")
print(animals)


#Insert element at specific index

animals.insert(3, "fruit fly")
print(animals)



last_animal=animals.pop()
print(animals)

