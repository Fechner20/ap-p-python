

def only_ints(a,b):
    if type(a) == int and type(b) == int:
        return True
    else:
        return False
z = only_ints(1,2)
print(z)

x = only_ints("j",3)
print(x)
