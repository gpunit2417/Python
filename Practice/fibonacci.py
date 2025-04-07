a = 0
b = 1
print(a, b, end=" ")
n = 5
i = 0
while(i<n):
    c = a+b
    print(c, end = " ")
    a = b
    b = c
    i += 1