"""
A semiprime number is a natural number that is the product of exactly two (not necessarily distinct) primes.

For example:
Input: 57
Output: true (57 is a semiprime number because it is the product of two primes, 57 = 3 * 19)

Input: 121
Output: true (121 is a semiprime number because it is the product of two primes, 121 = 11 * 11)

Input: 186
Output: false (186 is not a semiprime number because it is the product of three primes: 186 = 2 * 3 * 31)
"""
def prime_check(n):
    if n <= 1:
        return False
    for x in range(2,n):
        if n % x == 0:
            return False
    else:
        return True
        
def semiprime(n):
    if n < 1:
        return False
    for i in range(2,n):
        if n % i == 0:
            j = int(n/i)
            p1 = prime_check(i)
            p2 = prime_check(j)
            if p1 == True and p2 == True:
                return True
    else:
        return False
        
print("57 is a semiprime number: " + str(semiprime(57)))
print("121 is a semiprime number: " + str(semiprime(121)))
print("186 is a semiprime number: " + str(semiprime(186)))

def semiprime_gen(n):
    for num in range(2,n):
        check = semiprime(num)
        if check == True:
            yield num

print("")
print("The semiprime numbers in range are:")
for i in semiprime_gen(200):
    print(i)
