answer = 9
No_Of_Attempts = 1

while No_Of_Attempts <= 3:
    guess = int(input("Enter a number within the range (1-15): "))  
    if guess == answer:
        print("You Won")
        break
    else:
        No_Of_Attempts += 1
        if No_Of_Attempts <= 3:
            print(f"Sorry, you guessed the wrong number :(")
        else:
            print("You have no more attempts left! BETTER LUCK NEXT TIME!!!!")
