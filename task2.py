#Write a python program to sort a string alphabetically and print the count of each character.

def sort_and_count(str):
    sort_s = ''.join(sorted(str))  
    count = {}
    
    for char in sort_s:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
            
    return sort_s, count

s=input("Enter a string: ")
a,b=sort_and_count(s)
print("Sorted string:", a)
print("Character count:", b)
