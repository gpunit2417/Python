# import math
# print(math.gcd(12, 15))

a = 12
b = 15
def gcd(a, b):
    if b == 0:
        return a

    return gcd(b, a%b)

print(gcd(a, b))