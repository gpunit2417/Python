# password = "Secure3P@ss"
# password_length = len(password)

# if len(password) < 6:
#     strength = "Weak"
# elif len(password) <= 10:
#     strength = "Medium"
# else:
#     strength = "Strong"

# print("Password strength is: ", strength)

import string

password = "Secure3P@ss"
password_length = len(password)

# Criteria checks
has_upper = any(char.isupper() for char in password)
has_lower = any(char.islower() for char in password)
has_digit = any(char.isdigit() for char in password)
has_special = any(char in string.punctuation for char in password)

# Determine strength
if len(password) < 6 or not (has_upper and has_lower and has_digit and has_special):
    strength = "Weak"
elif len(password) <= 10:
    strength = "Medium"
else:
    strength = "Strong"

print("Password strength is:", strength)
