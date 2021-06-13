'''
Guess the number program. The objective is to guess a random number from 1 to 100. 
'''
import random

def maingame():
    print("Welcome to Guess the number")
    print("I'm thinking of a random number from 1-100.")
    print("Try guessing it!\n")

    random_number = random.randint(1,100)
    #print(f"(Testing: number is {random_number})")

    while True:
        difficulty = input("Choose your difficulty(easy/hard): ")

        if difficulty == 'easy':
            print("Easy difficulty selected. You have 10 guesses.")
            n_of_guesses = 10
            break
        elif difficulty == 'hard':
            print("Hard difficulty selected. You have 5 guesses.")
            n_of_guesses = 5
            break
        else:
            print("Invalid input, try again")
            continue

    guess = 0

    while n_of_guesses > 0:
        try:
            guess = int(input("\nMake a guess: "))
        except:
            print("Invalid input")
            continue
        if guess > random_number:
            n_of_guesses -= 1
            print(f"Too high. {n_of_guesses} guesses remaining.")
        elif guess < random_number:
            n_of_guesses -= 1
            print(f"Too low. {n_of_guesses} guesses remaining.")
        elif guess == random_number:
            print("You got it! Congratulations.")
            break

    replay = input("Want to play again?(y/n): ")
    if replay == 'n':
        print("Goodbye")
    else:
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
        maingame()
        
maingame()
