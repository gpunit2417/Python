num1 = int(input("Enter first number: "))  
num2 = int(input("Enter second number: "))  
flag = bool(int(input("Enter 1 for True or 0 for False: ")))  # Convert input to boolean  

if ((num1 < 0 and num2 > 0 and not flag) or (num1 > 0 and num2 < 0 and not flag) or (num1 < 0 and num2 < 0 and flag)):  
    print("True")  
else:  
    print("False")  
