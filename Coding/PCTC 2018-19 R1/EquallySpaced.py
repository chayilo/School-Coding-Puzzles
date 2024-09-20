num1 = int(input("Input the first number in the sequence:"))
num2 = int(input("Input the second number in the sequence:"))
num3 = int(input("Input the third number in the sequence:"))
num4 = int(input("Input the fourth number in the sequence:"))

if num1-num2 == num2-num3 == num3-num4:
    print(-(num1-num2))
else:
    print("NO")