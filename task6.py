#Create a function that checks whether given string is an anagram or not

def anagram(str1, str2):
    if len(str1) != len(str2):
        return "They are not anagrams."
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    if sorted(str1) == sorted(str2):
        return "They are anagrams."
    else:
        return "They are not anagrams."
    
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
print(anagram(s1, s2))
