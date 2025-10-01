#Write a python function to encrypt a string using Ceasar’s Cipher

def cipher(s, shift):
    en = []
    for i in s:
        if i.isalpha():
            if i.isupper():
                base = ord('A') 
            else:
                base = ord('a')
            i = chr((ord(i) - base + shift) % 26 + base)
            en.append(i)
        else:
            en.append(i)
    return ''.join(en)   

s = input("Enter a string: ")
shift = int(input("Enter shift value: "))
encrypted_str = cipher(s, shift)
print("Encrypted string:", encrypted_str)

