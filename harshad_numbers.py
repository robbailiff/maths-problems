"""
A harshad number (or Niven number) is an integer that is divisible by the sum of its digits.

For example:
Input: 18
Output: true (18 is a Harshad number because it is divisible by the sum of its digits: 18 = (1 + 8) x 2)

Input: 1729
Output: true (1729 is a Harshad number because it is divisible by the sum of its digits: 
1729 = (1 + 7 + 2 + 9) × 91)

Write a program to check if the user input is a Harshad number or not.
"""

def harshad(n):
    n_lst = []
    for i in str(n):
        n_lst.append(int(i))
    total = sum(n_lst)
    if n % total == 0:
        return True
    else:
        return False

print(harshad(1729))

def harshad_range(n):
    harshad_nums = []
    for x in range(1, n):
        num = harshad(x)
        if num == True:
            harshad_nums.append(x)
    return harshad_nums 
    
print(harshad_range(1000))
