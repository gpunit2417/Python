# str1 = "abba"

# str2 = ''.join(reversed(str1))

# if(str1 == str2):
#     print("Palindromic")
# else:
#     print("Not Palindromic")

str1 = "abba"

if str1 == str1[::-1]:  # Reverse the string using slicing
    print("Palindromic")
else:
    print("Not Palindromic")
