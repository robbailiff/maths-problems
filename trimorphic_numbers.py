"""
A trimorphic number is a number whose cube ends in the number itself. 

For example:
Input: 4
Output: true (4^3 is 64, which ends in 4)

Input: 24
Output: true (24^3 = 13824)

Input: 249
Output: true (249^3 = 15438249)

"""

def trimorphic(n):
    l = len(str(n))
    cube = str(n**3)
    if cube[-l:] == str(n):
        print(f"{n} is a trimorphic number")
    else:
        print(f"{n} is NOT a trimorphic number")

trimorphic(4)
trimorphic(10)
trimorphic(24)
trimorphic(249)

def trimorphic_gen(n):
    for x in range(1,n):
        l = len(str(x))
        cube = str(x**3)
        if cube[-l:] == str(x):
            yield x

print("")
print("List of trimorphic numbers in range:")
for i in trimorphic_gen(100):
    print(i)
