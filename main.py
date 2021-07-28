import random
randnum=random.randint(1,100)
userguess=None
guesses=0

while(userguess!=randnum):
    userguess=int(input("Enter your guess: "))
    guesses+=1
    if(userguess==randnum):
        print("You guessed it right!")
    else:
        if(userguess>randnum):
            print("You guessed it wrong! Smaller number please")

        else:
            print("You guessed it wrong! Larger number please")
            

print(f"You guessed the number in {guesses} guesses")

with open("highscore.txt", "r") as f:
    highscore = int(f.read())

if(guesses<highscore):
    print("You have ejust broken the high score")
    with open("highscore.txt", "w") as f:
        f.write(str(guesses))

