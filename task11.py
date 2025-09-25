#Write a Python program that prints the grade level of a given text using Coleman-Liau formula.

def coleman_liau(text):
    letters = sum(c.isalpha() for c in text)
    words = len(text.split())
    sentences = sum(c in '.!?' for c in text)
    
    if words == 0:
        return "Text must contain at least one word."
    
    L = (letters / words) * 100
    S = (sentences / words) * 100
    
    index = 0.0588 * L - 0.296 * S - 15.8
    grade = round(index)
    
    if grade < 1:
        return "Before Grade 1"
    elif grade >= 16:
        return "Grade 16+"
    else:
        return grade
    
text = input("Enter the text: ")
result = coleman_liau(text)
print(result)