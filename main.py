


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    import random

    guess_number = random.randint(1, 100)
    guess = 0
    while guess != guess_number:
        guess = int(input("Welcome To The Guessing Game! I am thinking of number from 1 to 100! Can you Guess?"))
        if guess > guess_number:
            print("Wrong Guess,Guess Lower")
        elif guess < guess_number:
            print("Wrong Guess,Guess Higher")
    else:
        print("Congrats! You Have Won The Guessing Game")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
