number = int(input("Enter a Non Negative Number: "))
factorial = 1
i = 1
if number < 0:
    print("Factorial is not defined for negative number")
else: 
    while i <= number:
        factorial *= i
        i += 1
    print(f"The Factorial of the Number {number} is {factorial}")