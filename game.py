import random
playing = True 
number = str(random.randint(0,9))

print("I will guess a number from 0-9 and the game ends after you guess the number I guessed")
print("You will win the game after you guess what number I guess")

while playing:
   guess = input("Guess a number from 1-10. Give me your best guess!: ")
   if number == guess:
     print("Good Job! You win the game")
     print("The number was", number) 
     break

else:
   print("your guess wasn't quite right! Guess again.")