#Write a python program to check if given number is a hill number

def hill_number(num):
    n = len(num)
    
    if n < 3:
        return False  
    found = False
    for i in range(1, n):
        if not found:
            if num[i] > num[i - 1]:
                continue
            elif num[i] < num[i - 1]:
                found = True
            else:
                return False  # Equal adjacent digits
        else:
            if num[i] < num[i - 1]:
                continue
            else:
                return False  # Not strictly decreasing after peak
    
    return found

num=input("Enter a number: ")
if hill_number(num):
    print(num," is a hill number")
else:
    print(num," is not a hill number")
