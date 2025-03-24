num = int(input("Enter the number:\n"))

if num<0:
    while num != 0:
        print(num, end = " ")
        num = num + 1
else:
    while num != 0:
        print(num-1, end = " ")
        num = num - 1