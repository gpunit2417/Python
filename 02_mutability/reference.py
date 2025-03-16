list1 = [1, 2, 3]
print(list1)

list2 = list1
print(list2)

list1[1] = 4
print(list1)
print(list2)

list2 = [2, 3, 4]
print(list1)
print(list2)

# OUTPUTs
# [1, 2, 3]
# [1, 2, 3]
# [1, 4, 3]
# [1, 4, 3]
# [1, 4, 3]
# [2, 3, 4]