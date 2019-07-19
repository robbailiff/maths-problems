"""
An emirp is a prime number that results in a different prime when its decimal digits are reversed. 
For example, 13 is an emirp number because both 13 and 31 are prime numbers.

For example:
Input: 17
Output: true (17 and 71 are prime numbers)

Input: 113
Output: true (113 and 311 are prime numbers)

Input: 23
Output: false (23 is a prime number, but 32 is not)

"""

def check_prime(n):
    if n <= 1:
        return False
    for x in range(2,n):
        if n % x == 0:
            return False
    else:
        return True
            
print("39 is a prime number: " + str(check_prime(39)))
print("97 is a prime number: " + str(check_prime(97)))


def emirp(n):
    prime = check_prime(n)
    if not prime or n < 12:
        return False
    if prime:
        n = str(n)
        new_n = int(n[::-1])
        emirp = check_prime(new_n)
        if emirp:
            return True
        else:
            return False
        
print("113 is an emirp number: " + str(emirp(113)))
print("23 is an emirp number: " + str(emirp(23)))
print("")


def emirp_range(n):
    emirp_lst = []
    for num in range(2, n):
        e_num = emirp(num)
        if e_num:
            emirp_lst.append(num)
    return emirp_lst     

print(emirp_range(100))
