#Write a python function to check if a given credit card number is valid or not using Luhn’s Algorithm

def luhn(cn):
    cn = cn.replace(" ", "")
    if not cn.isdigit() or len(cn) < 2:
        return "Invalid credit card number."
    
    total = 0
    rev = cn[::-1]
    
    for i, digit in enumerate(rev):
        n = int(digit)
        if i % 2 == 1:
            n *= 2
            if n > 9:
                n -= 9
        total += n
    
    if total % 10 == 0:
        return "Valid credit card number."
    else:
        return "Invalid credit card number."
    
card = input("Enter credit card number: ")
result = luhn(card)
print(result)