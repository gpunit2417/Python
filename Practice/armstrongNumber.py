num = int(input("Enter the number:\n"))
n = num
sum = 0
while num > 0:
    digit = num % 10
    sum += (digit ** 3)
    num = num // 10

if n == sum:
    print("Armstrong")
else:
    print("Not an armstrong number")


# 153, 371, 54748 are armstrong numbers