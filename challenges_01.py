#PALINDROME CHECKER

word=input("Input any word: ")
if word == word[::-1]:
    print("Your word is a palindrome. ")
else:
    print("Your word is not a palindrome.")


#DOMAIN FROM EMAIL

email=input("Input your email: ")
atsign= email.index ("@")
domain=email[atsign+1::]
print(domain)


#FIRST AND LAST MATCH
mylist=["apples", "bananas", "mangos", "blueberrys"]
print(mylist)
question=input("Input the last Item of the list: ")
if question == mylist[3]:
    print("True")
else:
    print("False")


#CONDITIONAL SUFFIX ADDER

word1=input("Enter any word: ")
length= len(word1)
if length <= 3:
 print(word1)
elif word1[-3::] == "ing":
   print(word1+ "ly")
else:
    print(word1 + "ing")


