#Define a function named “triple_and” that takes three parameters and returns True only if they are all True and False otherwise

def triple_and(a,b,c):
    return bool(a) and bool(b) and bool(c)
a=input("Enter first value: ")
b=input("Enter second value: ")
c=input("Enter third value: ")
print(triple_and(a,b,c))
