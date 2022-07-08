#Python while loop:  you really cant tell the number f iterations required.
#example 1
# count = 0 
# while count < 9:
#     print("Number:", count)
#     count = count + 1
# print("Good bye!")


#Example two
# Guessing game
import random
n = 20
to_be_guessed = int(n+random.random())+1
guess = 0
while guess != to_be_guessed:
    guess = int(input("new number"))
    if guess > 0:
        if guess > to_be_guessed:
            print("Number too large")
        elif guess < to_be_guessed:
            print("Number too small")
    else:
        print("I'm sorry that you're giving up!")
        break
else:
    print("congradulations you made it.")