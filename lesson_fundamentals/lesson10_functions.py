#Python Functions: Blocks of code that can be reused.
# To run a function, you *call* the function by writing its name, followed by parenthesis, and any arguments it needs.

print("Functions (Procedures)")

print("\nExample 1")

def jim():
    print("Yo")

def joe():
    print("See you later alligator")

jim()
jim()
jim()
joe()

print("\nExample 2")

def express_this(e):# e is called a PARAMETER which is a placeholder for an ARGUMENT
    return e

expression = express_this(69+67-95) 
print(expression)
expression2 = express_this(69-2)
print (expression2)

def greeter(n):
    return f"Hi {n}!"

first = greeter("jim")
second = greeter("Negative Nancy")
third= greeter("Positive Polly")

print(first, second, third)



print("\n Example 4")

def remainder(a,b):
    return a % b

result = remainder(3,2)
print("Remainder: ", result)


print("\n Example 5")

def is_far(distance):
    #INSERT BASE CASE
    if distance < 0:
        return "Error"
    elif distance >= 100:
        return "That's far"
    elif distance <100 and distance >= 20:
        return "Thats not too far"
    elif distance < 20:
        return "That's nearby!"
   
        
print(is_far(0))



def double_sequencer(number, times):
    value = number
    sequence = []

    for i in range(times):
        value = value * 2
        sequence.append(value)

    return sequence

result = double_sequencer(6,7)
print(result)



#CHALLENGES


# Calculator PSEUDO CODE
#Multiply = (1st number, 2nd number)
#Answer=(1st number times the 2nd number)
#Display Answer

#Divide = (1st number, 2nd number)
#Answer=(1st number divided by the 2nd number)
#Display Answer

#Add = (1st number, 2nd number)
#Answer=(1st number plus the 2nd number)
#Display Answer

#Subtracts = (1st number, 2nd number)
#Answer=(1st number minus the 2nd number)
#Display Answer

def multiply(x,y):
    return x*y

def divide(x,y):
    return x/y

def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

calculator= multiply(5,6)
print(calculator)

calculator= divide(12,6)
print(calculator)

calculator= add(5,6)
print(calculator)

calculator= subtract(10,6)
print(calculator)


# AVERAGE CHALLENGE PSUEDO CODE
#Average =(1st number, 2nd number, 3rd number)
#(1st number +2nd number +3rd number)/3

#Display Average

def average(x,y,z):
    return(x+y+z)/3

av=average(2,10,17)
print(av)


#EVEN OR ODD CHALLENGE
#IS EVEN= Number
#Remain=Number modulus 2
# If remain is equal to 0:
#   the number is even
#Otherwise its odd

def eo(x):
    remain= x % 2
    if remain == 0:
        return "Even"
    else:
        return "Odd"



eoo = eo(8)
print(eoo)


#ANYLYZE WORD CHALLENGE

def anylyzeword(x):
    word = x
    vowelcount=0
    consonantcount=0
    for vowel in word:
        if vowel == "a" or vowel == "e" or vowel== "i" or vowel==  "o" or vowel==  "u" or vowel == "y":
            vowelcount = vowelcount + 1
        else:
            consonantcount= consonantcount + 1
    return f" In the word {word} there are {vowelcount} vowels and {consonantcount} consonants."
    


wordstats=anylyzeword("James")
print(wordstats)






