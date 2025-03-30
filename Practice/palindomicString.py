str1 = "abba"

str2 = ''.join(reversed(str1))

if(str1 == str2):
    print("Palindromic")
else:
    print("Not Palindromic")