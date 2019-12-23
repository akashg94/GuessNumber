from random import randint

for x in range(1, 6):
    guessNumber = int(input("Enter guess between 1 to 10 :"))
    randomNumber = randint(1, 10)

if guessNumber == randomNumber:
    print("You won")
else:
    print("sorry")
    print("random number was : ", randomNumber)
