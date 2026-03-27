def median(val,min,max):
    if val <= max and val >= min:
        return val
    elif val < min:
        return min
    else:
        return max 

x = median(3,18,13)
print(x)


    