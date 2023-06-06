# create rock scissors paper program that asks for user input
# 0 = rock 1 = scissors 2 = paper

import random

def whatIsIt(num):
  if num < 0 or num > 2: 
    return "You gave a wrong number! Number has to be between 0 and 2"
  choices = ["Rock", "Scissors", "Paper"]
  return choices[num]

#gives back 0-2 at random
def computerChoice():
  return random.randint(0, 2)

def rockScissorsPaper():
  #Code Here

  choice = input ("Choose rock or scissors or paper:")
  print(Choice)

# if statement that checks if user's chouse is correct

  if choice == "Rock" or  choice == "Scissors" or choice == "Paper":
    print("Your response is valid")
  else:
    print("Your response is not valid")
#computer choice
  computer_choice = whatIsIt(computer_choice)
  #print tie if user and computer response is the same

  computer_response = whatIsIt(computer_response)

  #print random computer response
  #print(whatIsIt(computerChoice()))




