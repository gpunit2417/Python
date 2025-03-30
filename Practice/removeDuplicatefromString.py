# str1 = "geEksforGEeks"
# str2 = ""

# for i in str1:
#     if i not in str2:  # Proper way to check if char is already present
#         str2 += i  # Append unique characters

# print(str2)


str1 = "geEksforGEeks"
str2 = "".join(set(str1))  # Set removes duplicates
print(str2)

# But this does not guarantee the original order.