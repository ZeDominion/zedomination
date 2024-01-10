import random


number_to_guess = random.randint(1, 10)

while True:
    # Pakt de guess van user
    guess = int(input("Guess a number between 1 and 10: "))

    # Check voor de guess
    if guess < number_to_guess:
        print("Te laag!")
    elif guess > number_to_guess:
        print("Te hoog")
    else:
        print("Congratulations! Goed geraden!")
        break