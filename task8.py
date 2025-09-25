#Write a python program to divide a given string into equal parts containing n(user input) characters of same sequence. Example: string=“abcdabcdabcdabcd” n=4 output: “abcd”, “abcd”, “abcd”, “abcd” If the division is not possible or the sequence cannot be same, print out the appropriate error.

def divide(str,num):
    length = len(str)
    if length % num != 0:
        return "Division not possible."
    
    part = str[:num]
    return [part] * (length // num)

s = input("Enter a string: ")
n=int(input("Enter the number of characters:"))
div = divide(s, n)
print("Divided parts:", div)

