#Find the fabonacci of a given number using recursion.

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

num = int(input("Enter a number: "))
fib=fibonacci(num)
print("Fibonacci number at position" , num," is", fib)
