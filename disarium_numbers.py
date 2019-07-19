"""
A number is called a Disarium number if the sum of the powers of its digits equals the number itself. The digits are powered to their positions in the number.

For example:
Input: 135
Output: true
135 is a Disarium number because it equals to 1^1 + 3^2 + 5^3 (each digit powered to the position in the number).

"""

def disarium(n):
    if n < 10:
        return False
    p_list = []
    for i, x in enumerate(str(n)):
        p_list.append(int(x)**(i+1))
    if n == sum(p_list):
        return True
    else:
        return False
    
print("44 is a disarium number: " + str(disarium(44)))
print("135 is a disarium number: " + str(disarium(135)))
print("")


def disarium_range(n):
    d_list = []
    for x in range(n):
        d = disarium(x)
        if d:
            d_list.append(x)
    return d_list 

print(disarium_range(1000))
