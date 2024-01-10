
while True:
    name = input("Enter your name: ")
    print(f"Hello, {name}!")

    age = input("What is your age?: ")
    print(f"Ahhh {age} years old!!")

    sex = input("What is your sex?: ")
    print(f"Alright, so you are {name}. {age} years old and you are an {sex}. Am i correct?")

    confirmation = input("Enter 'yes' if this is correct or 'no' if this is incorrect")
    if confirmation.lower() == 'yes':
        break

print("Thank you for confirmed the details")
