# call a built in random library for randomness
import random

# initial value of points for computer and user
user_points = 0
python_points = 0
game = ["Rock", "Paper", "Scissors"]

# while loop for user input that only work if the value of user points or python points not equal to 10
while user_points!= 10 and python_points != 10:
   try:
      u_turn = input("input a choice (Rock, Paper, Scissors): ").strip().capitalize()
      game.index(u_turn)
      p_turn = random.choice(game)

   # repeat the loop again if the user input value that not found in variable game 
   except ValueError:
      continue

   # after checking that the user is  valid, determine the the winner for each round in this game  
   else:
      if u_turn == "Paper" and p_turn == "Rock" or u_turn == "Scissors" and p_turn == "Paper" or u_turn == "Rock" and p_turn == "Scissors":
         user_points += 1
         print("you win!")

      elif u_turn == p_turn:
         user_points += 1
         python_points += 1
         print("this round become draw")

      else:
         python_points += 1
         print("python win!!")

# when one of the players get 10 points from played rounds computer print who is the winner
if user_points == 10:
   print("you win the game!")

elif python_points == 10:
   print("python win the game!!")
   
   


   
