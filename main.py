import random

logo='''
░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░░▒▓███████▓▒░▒▓███████▓▒░            ░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░            ░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓██████████████▓▒░░▒▓███████▓▒░░▒▓████████▓▒░▒▓███████▓▒░  
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░     ░▒▓█▓▒░                      ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░                   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░     ░▒▓█▓▒░                      ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░                   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒▒▓███▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓██████▓▒░  ░▒▓██████▓▒░░▒▓██████▓▒░                ░▒▓█▓▒░   ░▒▓████████▓▒░▒▓██████▓▒░              ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░░▒▓██████▓▒░ ░▒▓███████▓▒░  
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░             ░▒▓█▓▒░     ░▒▓█▓▒░               ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░                   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░             ░▒▓█▓▒░     ░▒▓█▓▒░               ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░                   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
 ░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓████████▓▒░▒▓███████▓▒░▒▓███████▓▒░                ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░            ░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░ 
                                                                                                                                                                                                                        
                                                                                                                                                                                                                        '''

print(logo)
print("Welcome to the number guessing game!\nI'm thinking of a number between 1 and 100.\n")

number=random.randint(1,100)

ask=input("Choose a difficulty. Type 'easy' or 'hard': ")

keep_trying=True

if ask=='easy':
  attempts=10
  print(f"You have {attempts} attempts remaining to guess the number.")
  while keep_trying:
    while attempts>0:
      ask2=int(input("Make a guess: "))
      if ask2<number:
        attempts-=1
        if attempts>0:
          print(f"Too low.\nGuess again.\nYou have {attempts} attempts remaining to guess the number.\n")
        else:
          print("You've run out of guesses, you lose.\n")
      elif ask2>number:
        attempts-=1
        if attempts>0:
          print(f"Too high.\nGuess again.\nYou have {attempts} attempts remaining to guess the number.\n")
        else:
          print("You've run out of guesses, you lose.\n")
      elif ask2==number:
        print(f"You got it. The answer was {number}.\n")
        keep_trying=False
        break

elif ask=='hard':
  attempts=5
  print(f"You have {attempts} attempts remaining to guess the number.")
  while keep_trying:
    while attempts>0:
      ask2=int(input("Make a guess: "))
      if ask2<number:
        attempts-=1
        if attempts>0:
          print(f"Too low.\nGuess again.\nYou have {attempts} attempts remaining to guess the number.\n")
        else:
          print("You've run out of guesses, you lose.\n")
      elif ask2>number:
        attempts-=1
        if attempts>0:
          print(f"Too high.\nGuess again.\nYou have {attempts} attempts remaining to guess the number.\n")
        else:
          print("You've run out of guesses, you lose.\n")
      elif ask2==number:
        print(f"You got it. The answer was {number}.\n")
        keep_trying=False
        break
