"""
A composite number is a positive integer that is not prime. In other words, it is a positive integer that has at least one divisor other than 1 and itself. The composite numbers up to 20 are 4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20.

For example:
Input: 10
Output: yes (10 has divisors other than 1 and itself, for example, 2 or 5).

Input: 5
Output: no (5 is a prime number because it has no other divisors other than 1 and itself).

Write a program to check if the user input is a composite number or not.
"""

def composite(n):
    if n <= 1:
        print("1 is a NOT a composite number")
        return
    for x in range(2,n):
        if n % x == 0:
            print(f"{n} is a composite number")
            break
    else:
        print(f"{n} is a prime number")
            
composite(1)            
composite(2)
composite(39)
composite(97)


def composite_range(n):
    
    composites = []
    for num in range(2, n):
        for x in range(2, num):
            if num % x == 0:
                composites.append(num)
                break
    return composites     

print(composite_range(100))
