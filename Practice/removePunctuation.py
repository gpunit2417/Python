import string
s = "hello, world!"
for i in "".join([c for c in s if c not in string.punctuation]):
    print(i, end="")