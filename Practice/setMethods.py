set1 = {1, 2, 3, 4, 5}
set2 = {3, 3, 5, 8, 7, 9, 6}

# set1.add(2)
# print(set1)
# #{1, 2, 3, 4, 5}

# set1.add(7)
# print(set1)
# #{1, 2, 3, 4, 5, 7}

# set1.pop()
# print(set1)
# #{2, 3, 4, 5, 7}

# set1.remove(5)
# # set1.remove(7)    #KeyError
# print(set1)

# print(set2)   #prints all unique from the set

print(set1.intersection(set2))

print(set1.union(set2))

print(set2.difference(set1))

print(set1.difference(set2))