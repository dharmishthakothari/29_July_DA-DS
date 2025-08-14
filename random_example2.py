import random

ran_number=random.randint(1,100)

while True:
    guess=int(input("Please guess number "))
    if guess==ran_number:
        print("You have guess right number ")
        break