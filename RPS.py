print("Rock Paper Scissors")

mes1 = input("player one chooses ---- ")
mes2 = input("player two chooses ---- ")

if mes1 == "Rock" or "rock" and mes2 == "Paper" or "paper":
    print("player two wins")

if mes1 == "Rock" or "rock" and mes2 == "Scissors" or "scissors":
    print("player one wins")

if mes1 == "Paper" or "paper" and mes2 == "Rock" or "rock":
    print("player one wins")

if mes1 == "Paper" or "paper" and mes2 == "Scissors" or "scissors":
    print("player two wins")

if mes1 == "Scissors" or "scissors" and mes2 == "Rock" or "rock":
    print("player two wins")

if mes1 == "Scissors" or "scissors" and mes2 == "paper" or "paper":
    print("player two wins")

if mes1 == mes2:
    print("there has been a tie")

print("do you want to restart? if so then stop being lazy and DO IT YOUR SELF!")



