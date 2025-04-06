string = input("Enter the string:\n")
vowels = [sum(1 for c in string if c in 'aeiou')]
for i in vowels:
    print(i, end=" ")