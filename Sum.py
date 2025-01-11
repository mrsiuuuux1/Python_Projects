num1 = 1
num2 = 1

while num1 > 0 and num2 > 0:
    num1 = int(input("Enter your first number: "))
    num2 = int(input("Enter your second number: "))
    if num1 > 0 and num2 > 0:
         sum = num1 + num2
         print(f"The sum of two numbers is {sum}")
    else:
        print("The Program has been Terminated")