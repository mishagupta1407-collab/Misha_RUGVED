#Write a program to print the Fibonacci Sequence till n-values where n is user input.

def fibonacci(n):
    a, b = 0, 1
    sequence = []

    for i in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence


num = int(input("Enter the number of terms: "))
if num <= 0:
    print("Please enter a positive integer.")
else:
    fs = fibonacci(num)
    print("Fibonacci Sequence:",fs)
        