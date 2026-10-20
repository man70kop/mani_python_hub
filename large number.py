num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))
num3 = int(input("enter third number: "))
if num1 < num2 and num3 < num2:
    print("largest number is", num2)
elif num1 < num3 and num2 < num3:
    print("largest number is", num3)
else:
    print("largest number is", num1)