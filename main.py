# ROCK, PAPER, SCISSORS Game
import time

print("Starting the Nvidia Game Engine...!")
time.sleep(5)
print("Game Engine Started...!")
time.sleep(2)
print("CPU load exceeding...!")
time.sleep(7)
print("Starting RPS Game Engine - 17.3 GB")
print("Starting...!")
time.sleep(9)
print("Done!")
time.sleep(8)

while True:
    uinput = str(input("Enter 'rock', 'paper' or 'scissors': "))
    
    if uinput.lower() == "rock":
        print("Nvidia Server: Paper")
        print("You Lose!\nPoop Boy!")
    elif uinput.lower() == "paper":
        print("Nvidia Server: Scissors")
        print("You Lose!\nPoop Boy!")
    elif uinput.lower() in ["scissors", "scissiors"]:
        print("Nvidia Server: Rock")
        print("You Lose!\nPoop Boy!")
    else:
        print("You foolish fellow!\nYou don't know how to write 'rock', 'paper' or 'scissors'!")
        print("Reconnecting...")
        time.sleep(5)
        break
