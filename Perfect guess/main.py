import random

randNumber = random.randint(1, 100)
userGuess = None
guesses = 0

while (userGuess != randNumber):
    userGuess = int(input("Enter Your Guess: "))
    guesses +=1 

    if (userGuess == randNumber):
            print("You guessed is right!")

    else:
        if (userGuess>randNumber):
             print("You guessed it wrong! Enter a smaller number")

        else:
            print("You guessed it wrong! Enter a Large number")


print(f"You guessed the number in {guesses} guesses")
with open("hiscore.txt","r")as f:
     hiscore = int(f.read())

if (guesses<hiscore):
     print("You have just broken the high score!")
     with open("hiscore.txt","w")as f:
          f.write(str(guesses))