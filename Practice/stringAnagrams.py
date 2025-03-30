# from collections import Counter

# str1 = "Punit"
# str2 = "Punit"

# # Convert to lowercase to make it case-insensitive (optional)
# if Counter(str1) == Counter(str2):
#     print("Anagrams")
# else:
#     print("Not Anagrams")


str1 = "Punit"
str2 = "punit"

if sorted(str1.lower()) == sorted(str2.lower()):
    print("Anagrams")
else:
    print("Not Anagrams")
