# Import modules
import random

# Define variables
guesses = 0
number = random.randint(0, 10)

# Introduction of the Game
print("Welcome to the Game of Luck, you will get only 3 chances for guessing my number")
name=input("\nEnter your name : ")
print("\n"+name+" I am thinking of a number between 1 - 10")

# Main program loop
while( guesses < 3 ):
  choice = eval(input("\nHave a guess "+name+" : "))
  
  if (choice == number):
    print("\nCongratulations Buddy!\n")
    break
  
  elif (choice > number or choice < number):
    print("\nYour guess is not correct")
    guesses = guesses + 1

  elif (choice == 0):
    print("\nYou surely got a 0 in all the exams throughout your life!!\n")
    break
  else:
    print("\nIdiot!! You are certainly from another planet, since you dont understand English...\n")
    break

if guesses == 3:
    print("\nYou lose!")
    print("The number I was thinking of was: " + str(number))


