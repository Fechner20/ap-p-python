#LISTS IN PYTHON
#Lists store multiple values in one variable.
#They are ordered,mutable (changeable), and allow duplicates

print()
print("---Lists in Python---")


empty_list = []
empty_list.append("Thing")
print(empty_list)


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

animal_to_replace = animals.index("Blobfish")
print(animal_to_replace)
animals[animal_to_replace]= "seamonkey"
print(animals)


nums = [3, 7, 4, 1, 5, 9, 2, 8, 6, 0]
print("Original Numbers: ", nums)

print("Length of list: ",len(nums))
print("Min: ", min(nums))
print("Max: ", max(nums))
print("Sum: ", sum(nums))

nums.sort()
print(nums)


nums.reverse()
print(nums)

if "cat" in animals:
    print("Cat is in the list!")
else:
    print("Cat is not in the list.")

original_list = [1, 2, 3]
copied_list = original_list.copy()
copied_list.append(4)
print(original_list)
print(copied_list)

matrix = [ [1, 2, 3],
           [4, 5, 6],
           [7, 8, 9] ]

print(matrix[2][2])


#CHALLENGE 1

integers= [1, 2, 3, 4, 5, 6]
swap=int(input("Input any integer: "))
swapping=integers.index(3)
integers[swapping]= swap
print(integers)


#CHALLENGE 2

shopping=[]
shopping.append("Eggs")
shopping.append("Pickles")
shopping.append("Ketchup")
shopping.remove("Ketchup")
print(shopping)

