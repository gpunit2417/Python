# mind blowing question
def function(a, b=[]):
    b.append(a)
    return len(b)

print(function(1))
print(function(2, []))
print(function(3))