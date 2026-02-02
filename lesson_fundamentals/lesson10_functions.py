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