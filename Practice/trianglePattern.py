# for i in range(1, 6): 
#     print("*" * i)

# for i in range(5, 0, -1): 
#     print("*" * i)

# for i in range(1, 6): 
#     print(" ".join(str(j) for j in range(1, i+1)))


# mind blowing question
def function(a, b=[]):
    b.append(a)
    return len(b)

print(function(1))
print(function(2, []))
print(function(3))