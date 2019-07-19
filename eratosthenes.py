"""
This is my attempt to make a prime number generator using the Sieve of Eratosthenes. 

For those who don't know what the Sieve of Eratosthenes is:

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

(https://www.smartickmethod.com/blog/math/operations-and-algebraic-thinking/divisibility/prime-numbers-sieve-eratosthenes/)

The Sieve of Eratosthenes is a process to find prime numbers. A prime number is one which is only divisible by 1 and itself. The idea behind the Sieve of Eratosthenes is to find numbers in a grid that are multiples of a number and therefore composite, to discard them as prime. The numbers that are left will be prime numbers.

The Sieve of Eratosthenes stops when the square of the number we are testing is greater than the last number on the grid.

"""

def Sieve_of_Eratosthenes(n):
    
    for i in range(2, n):   # Finds the square that is greater than the last number in range
        if i**2 > n:
            square = i
            break
            
    primes = []
    for number in range(2, n+1):    # Iterates through all the numbers within input range

        count = 2    
        for x in range(2, square+1):    # For each number, iterates through the dividing numbers
            
            if number != x and number % x == 0: # Filters any number that has a divisor that is not itself
                break
                
            elif count == square:   # Appends any number that has iterated through all the dividing numbers and has no divisors
                primes.append(number)
                
            elif number != x and number % x != 0: # Adds a count for each dividing number that is not a divisor
                count+=1
                continue
    
            else:   # Appends any number that is smaller than the number highest square and has no divisors
                primes.append(number)
                break

    #return primes
    for prime in primes:
        yield prime

#print(Sieve_of_Eratosthenes(100))
for x in Sieve_of_Eratosthenes(100):
    print(x)
