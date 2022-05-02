import  random
number_to_guess = [18, 5, 100, 69, 70, 21]
a = random.choice(number_to_guess)
number_of_guesses = 6
while(1):
    number_of_guesses = number_of_guesses - 1
    print("Guess a number, you have",number_of_guesses,"chances")
    number_you_guess = int(input())

    if number_of_guesses == 0:
        print("!!GAME OVER!!")

    elif number_you_guess > a:
        print("Its greater than the number you have to guess")
        continue
    elif number_you_guess == a:
        print("Congratulations, you guessed the correct number",)

    else:
        print("Its less than the number you have to guess")
        continue
    # while(1):
    print("Enter Y to play again or N to end the game")
    b = input()
    if b == 'Y':
        continue
    else:
        break

