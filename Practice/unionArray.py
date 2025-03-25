lst1 = [12, 43, 455, 554, 32, 23, 12]
lst2 = [12, 45, 223, 454, 78, 23, 332, 664]
a = set(lst1)
b = set(lst2)
# print((list(a.union(b))))
# print(len(list(a.union(b))))

print(list(a.intersection(b)))
print(len(list(a.intersection(b))))