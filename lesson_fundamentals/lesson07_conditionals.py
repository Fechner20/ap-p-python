#CONDITIONALS IN PYTHON
# comparison operaters: ==, != , <, >, <=, >=
# logical operaters: and, or, not
#control flow: elif, if, else


print("---Conditionals in Python---")
print(3==2)
print("Hello" == "Hi There")
print(7!= 4)
print(4>5)


#if

num=10
if num == 10:
    print("Your number is equal to 10")


    num2 = 13
    print(num2 <= 12)
    if num2 <= 12:
        print("Your number is less thna or equal to 12")
    else:
        print("Your number is greater than 12")

    #if elif else

    temperature = 93
    if temperature > 80:
        print("Its Hot!")
    elif temperature >= 60:
        print("Its Nice")
    else:
        print("Its cold!")


    x=2
    y=20

    if x==y:
        print("x is equal to y")
    elif x>y: 
        print("x is greater than y")
    elif x<y:
        print("x is less than y")
    else:
        print("error")

# Logical operater: and, or, not
#both sides of the 'and' must be true, otherwise it's false



age=17
has_permission=False

if age >= 17 and has_permission:
    print("You can drive")
else:
    print("Can't drive yet")

    #Using "or " and "not"

    day= "Monday"
    

    if day == "Saturday" or day == "Sunday":
        print("Its the weekend!")
    elif day == "Monday" or "Tuesday":
        print("It's Monday or Tuesday!")
    else:
         print("It's Wed,Thur , or Fri")


    if day is not "Monday":
        print("It's not Monday")

#Challenge 1

#Modulous returns remainder
 
number=int(input("Pick any number: "))
if number % 2 is 0:
    print("Your number is even")
else:
    print("Your number is odd")    

#Challenge 2
password="VHSHockeyRocks"
pw=input("Password: ")
if password != pw:
    print("Acsess Denied ")
else:
    print("Accses Granted")

#Challenge 3
grade=int(input("Gimme your numeric grade in AP CS Principles with Mr. Harrell: "))
if grade >= 90:
    print("You have an A in AP CS Principles with Mr. Harrell.")
elif grade >= 80:
    print("You have a B in AP CS Principles with Mr. Harrell.")
elif grade >= 70:
    print("You have a C in AP CS Principles with Mr. Harrell.")
elif grade > 60:
    print("You have a D in AP CS Principles with Mr. Harrell.")
else:
    print("You have an F and you are failing AP CS Principles with Mr. Harrell.")