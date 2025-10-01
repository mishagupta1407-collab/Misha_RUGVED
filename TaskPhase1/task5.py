#Find the fabonacci of a given number using recursion.

# def fibonacci(n):
#     if n <= 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)

# num = int(input("Enter a number: "))
# fib=fibonacci(num)
# print("Fibonacci number at position" , num," is", fib)
#  def factorial(n):
#    if n==1:
#       return 1
#    else:
#       return n*factorial(n-1)

def countw(s):
   count=1
   length=len(s)
   for i in range (length):
      if (s[i]==' '):
         count+=1
   i+=1
   return count

str=input("Enter a sentence:")
num=countw(str)
print("The number of words are ",num)
