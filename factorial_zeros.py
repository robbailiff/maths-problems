"""
The factorial of a non-negative integer n, denoted by n! is the product of all positive integers less than or equal to n. For example, 5! = 5 x 4 x 3 x 2 x 1 = 120.

Write a program to calculate the number of trailing zeros in n! where n is any positive number less than 10^7.

For Example:
Input: 5
Output: 1 (5! = 120 has one trailing zero)

Input: 10
Output: 2 (10! = 3628800 has two trailing zeroes)

"""

def factorial(x):
  if x <= 1:
    return 1
  else: 
    return x * factorial(x-1)

def fact_zero(n):
    numf = str(factorial(n))
    num = numf[::-1]
    count = 0
    for x in num:
        if x == '0':
            count += 1
        else:
            break
            
    print(f"The factorial of the number {n} is {numf}. The number of trailing zeroes is {count}.")        
    
    
fact_zero(5)
print("")
fact_zero(10)
