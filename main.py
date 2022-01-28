from art import logo,vs
from game_data import data
import random
from replit import clear

def formate_data(account):
  """3 Takes the account data and return in printable formate data."""
  account_name = account["name"]
  account_descr = account["description"]
  account_country = account["country"]
  return(f"{account_name}, a {account_descr}, from {account_country}")


##5 Use if statement of check if user is correct.

def check_answer(guess,a_follower,b_follower):
  """Take the user guess and follower count and return if they got it right."""
  if a_follower> b_follower:
    return guess == "a"
  else:
    return guess == "b"


#1Display logo
print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)

#Make the game repeatable.
while game_should_continue:
  #2Generate random account from game data.

  #7 Making account at position B become the next account at position A.
  account_a = account_b
  account_b = random.choice(data)
  while account_a==account_b:
    account_b = random.choice(data)

  print(f"Compare A : {formate_data(account_a)}")
  print(vs)
  print(f"Against B : {formate_data(account_b)}")

  #4Ask user for guess
  guess = input("Who has more follower?Type 'A' or 'B': ").lower()
  print(logo)
  clear()

  #5 Check if user got it right.
  ##5 Get follower count of each account.
  a_follower_count = account_a["follower_count"]
  b_follower_count = account_b["follower_count"]

  is_correct = check_answer(guess,a_follower_count, b_follower_count)

  #6 Give user the feedback on their guess.
  if is_correct:
    score+=1
    print(f"You're right! Current score: {score}.")
  else:
    game_should_continue = False
    print(f"Sorry,that's wrong. Final Score: {score}.")

#7 Making account at position B become the next account at position A.