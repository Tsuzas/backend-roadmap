import random

difficulty = int(input("""\nWelcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
You have 5 chances to guess the correct number.\n
Please select the difficulty level:
1. Easy (10 chances)
2. Medium (5 chances)
3. Hard (3 chances)\n
Enter your choice: """))

match difficulty:
    case 1:
        print("Great! You have selected the Easy difficulty level.")        
        attempts = 10
    case 2:
        print("Great! You have selected the Medium difficulty level.")        
        attempts = 5
    case 3:
        print("Great! You have selected the Hard difficulty level.")        
        attempts = 3
aiNumber = random.randint(1, 100)   
tries = 1
answer = ""
while attempts > 0:
    answer = int(input("\nEnter your guess: "))

    if aiNumber > answer:
        print(f"Incorrect! The number is greater than {answer}.")
        attempts -= 1
        tries += 1

    elif aiNumber < answer:
        print(f"Incorrect! The number is less than {answer}.")
        attempts -= 1
        tries += 1

    else:
        print(f"Congratulations! You guessed the correct number in {tries} attempts.")
        break
if attempts == 0:
    print(f"Bahh, you ran out of tries the number was {aiNumber}")