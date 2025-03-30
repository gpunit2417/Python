str1 = "[[]]"
str2 = "body"

half = int(len(str1) / 2)
print(str1[:half] + str2 + str1[half:])