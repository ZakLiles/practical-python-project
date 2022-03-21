import random
user_name = input("Howdy, what's your name?\n")

rand_num = random.randint(1,100)
print(user_name+", I'm thinking of a number between 1 and 100.\nTry to guess my number.")

guesses = 0
while True:
    user_guess = int(input("Your guess? "))
    guesses+=1
    if user_guess == rand_num:
        print("Well done, "+user_name+"! You found my number in "+str(guesses)+" tries!")
        break
    elif user_guess > rand_num:
        print("Your guess is too high, try again")
    else:
        print("Your guess is too low, try again")