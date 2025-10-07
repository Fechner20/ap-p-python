# Basic string creation and indexes:
greeting= "Hello"
name="Ada"
print(greeting,name)


# 0 1 2 3 4
# H E L L 0

#0 1 2
#A D A
print(greeting[3])

message=greeting + " " + name + "!!!"
print("Concatenated Message:", message)

word="loquacious"
print("First Letter: ", word[0])
print("Last Letter: ", word[-1])
print("Range of Letters(non-inclusive):", word[1:6])
print(word[:5])
print("Last seven letters" , word[-7:])
print("Step through every second characther:", word[::2])
print("Reversed, stepping every third letter:", word[::-3])

## Built in functions

country="Turkeminestan"
length_of_word=len(country)
print(length_of_word)

phrase="JaMEs"
print("\nUppercasse:",phrase.upper())
print("Lowercase: ", phrase.lower())
print("Capitillized:",phrase.capitalize())