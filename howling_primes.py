"""
A howling prime is a prime number if the sum of its digits is also a prime number.

For Example:
Input:113
Output: true (113 is a prime number, 1+1+3=5 is also a prime number)

Input: 89
Output: true (89 is a prime number, 8+9=17 is also a prime number)

Input: 19 
Output: false (19 is a prime number, but 1+9=10 is not a prime number)

Write a program to check if the user input is a howling prime or not.

"""

def prime(n):
    if n <= 1:
        return False
    for x in range(2,n):
        if n % x == 0:
            return False
    else:
        return True
        
        
def howling_prime(n):
    p = prime(n)
    if not p or n < 11:
        return False
    if p:
        list_n = []
        n = str(n)
        for i in n:
            list_n.append(int(i))
        total = sum(list_n)
        h_check = prime(total)
        if h_check:
            return True
        else:
            return False
            
            
def howling_gen(n):
    for x in range(n):
        h = howling_prime(x)
        if h:
            yield x
        

print("113 is a Howling Prime: " + str(howling_prime(113)))

print("89 is a Howling Prime: " + str(howling_prime(89)))

print("19 is a Howling Prime: " + str(howling_prime(19)))

print("")
print("The Howling Primes up to 200 are:")

for x in howling_gen(200):
    print(x)
