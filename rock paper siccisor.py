import random
print("              Welcome to Rock-Paper-Scissors Game!           ")
user_score = 0
computer_score = 0
choices = ["rock", "paper", "scissors"]
while True:
    print("    Choose: rock, paper, or scissors   ")
    user = input("Your choice: ").lower()
    if user not in choices:
        print("Invalid choice! Try again.")
        continue
    computer = random.choice(choices)
    print("Computer chose:", computer)
    if user == computer:
        result = "Tie!"
    elif (user == "rock" and computer == "scissors")or(user == "scissors" and computer == "paper")or(user == "paper" and computer == "rock"):
        result = "You win!"
        user_score += 1
    else:
        result = "Computer wins!"
        computer_score += 1
    print(result)
    print(f"Score → You: {user_score} | Computer: {computer_score}")
    play_again = input("Play again? (yes/no): ").lower()
    if play_again != "yes":
        print(f"your score : {user_score}")
        print(f"computer score : {computer_score}")
        if (computer_score > user_score):
            print(" SORRY  YOU LOSE!  ")
        elif (computer_score < user_score):
            print("  HURRAY  YOU WON   ")
        else:
            print("      IT'S  A  TIE   ")
        print("Thanks for playing!")
        break
