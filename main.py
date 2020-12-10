loose = ("The computer wins")
win = ("You win")
lives = 5
score = 0
drew = 0
computer_lives = 5

#Sadly, I couldn't do the big fancy logo that the instructor did so I had to make a smaller version.
print("Welcome to Rock, Paper Scissors!")
print("")
print("RULES:")
print("You will start with " + str(lives) + " lives.")
print("If you win the computer looses a life.")
print("If you loose then you loose a life.")
print("If you draw then the number of lives stays the same.")
print("Type \"display lives\" at any time to see how many lives you have left")
print("Type \"display score\" at any time to see your score")
print("Type \"display drew\" at any time to see your score")
print("Make sure to not use any capitals when playing.")
print("Can you win?")
print("Good luck!")
print("")
print("")

while true:
  rps = input("rock, paper, or scissors?   ")
  import random
  computer = ("rock", "paper", "scissors")
  computer = random.choice(computer)
  #Here are the if statements for rock
  if rps == "rock" and computer == "paper":
    print("The computer chose" + str(computer))
    print("")
    print(loose)
    print("")
    print("")
    lives -= 1
  if rps == "rock" and computer == "scissors":
    print("The computer chose" + str(computer))
    print("")
    print(win)
    computer_lives -= 1
    print("")
    print("")
    score += 1
  #Here are the if statements for paper
  if rps == "paper" and computer == "scissors":
    print("The computer chose" + str(computer))
    print("")
    print(loose)
    print("")
    print("")
    lives -= 1
  if rps == "paper" and computer == "rock":
    print("The computer chose" + str(computer))
    print("")
    print(win)
    computer_lives -= 1
    print("")
    print("")
    score += 1
  #Here are the if statements for scissors
  if rps == "scissors" and computer == "paper":
    print("The computer chose" + str(computer))
    print("")
    print(win)
    computer_lives -= 1
    print("")
    print("")
    score += 1
  if rps == "scissors" and computer == "rock":
    print("The computer chose" + str(computer))
    print("")
    print(loose)
    print("")
    print("")
    lives -= 1
  #Here are the if statements for duplicates
  if rps == "rock" and computer == "rock":
    print("The computer chose" + str(computer))
    print("")
    print("You drew")
    print("")
    print("")
    drew += 1
  if rps == "paper" and computer == "paper":
    print("The computer chose" + str(computer))
    print("")
    print("You drew")
    print("")
    print("")
    drew += 1
  if rps == "scissors" and computer == "scissors":
    print("The computer chose" + str(computer))
    print("")
    print("You drew")
    print("")
    print("")
    drew += 1
  #commands
  if rps == "display lives":
    print(lives)
  if rps == "display score":
    print(score)
  if rps == "display drew":
    print(drew)
  #lives
  if lives == 0 or rps == "test":
    print("You ran out of lives.")
    print("Thanks for playing!")
    print("Your score is" + str(score) + ".")
    print("You had " + str(drew) = " draws.")
    stop = input("Press enter to exit.")
  if computer_lives = 0:
    print("The computer ran out of lives. You Win!")
    print("Thanks for playing!")
    print("Your score is" + str(score) + ".")
    print("You had " + str(drew) = " draws.")
    stop = input("Press enter to exit.")