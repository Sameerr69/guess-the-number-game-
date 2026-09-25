import random
n = random.randint(1, 100)
guess = 0
a = 0
while a != n:
    a = int(input("Guess a number: "))
    guess += 1
    if a < n:
        print("Too low")
    elif a > n:
        print("Too high")
    else:
        print("Correct!")
print(f"You have guessed the number in {guess} tries")