"""
A Mersenne prime is a prime number that is one less than a power of two. It is a prime number of the form 2^n − 1 for some integer n.

For example:
Input: 3
Output: true (3 is a prime number and 3=2^2-1)

Input: 31
Output: true (31 is a prime number and 31=2^5-1)

Input: 17
Output: false (17 is a prime number but it is not of the form 2^n-1)

Write a program to check if the user input is a Mersenne prime or not.
"""

def prime(n):
    if n <= 1:
        return False
    for x in range(2,n):
        if n % x == 0:
            return False
    else:
        return True

def mersenne(n):
    for i in range(2,n):
        p = 2**i-1
        p_check = prime(p)
        if p_check and n == p:
            return True
    else:
        return False

def mersenne_gen(n):
    for i in range(n):
        m = mersenne(i)
        if m:
            yield i

print("3 is a Mersenne Prime: " + str(mersenne(3)))
print("31 is a Mersenne Prime: " + str(mersenne(31)))
print("17 is a Mersenne Prime: " + str(mersenne(17)))
