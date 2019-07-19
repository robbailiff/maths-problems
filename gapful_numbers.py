"""
A gapful number is a number of at least 3 digits that is divisible by the number formed by the first and last digit of the original number.

For Example:
Input: 192
Output: true (192 is gapful because it is divisible 12)

Input: 583
Output: true (583 is gapful because it is divisible by 53)

Input: 210
Output: false (210 is not gapful because it is not divisible by 20)

Write a program to check if the user input is a gapful number or not.

"""

def gapful(n):
    ns = str(n)
    if len(str(n)) >= 3:
        num = int(str(ns[0]) + str(ns[-1]))
        if n % num == 0:
            return True
        else: 
            return False 
    else:
        print("Number needs to be at least 3 digits long")
            
print(gapful(100))

def gapful_range(n):
    g_nums = []
    for x in range(100, n):
        num = gapful(x)
        if num == True:
            g_nums.append(x)
    return g_nums 
    
print(gapful_range(1000))
