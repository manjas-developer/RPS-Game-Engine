import random
import time

def play():
    print("Starting the Nvidia Game Engine...! 🎮🚀")
    time.sleep(2)
    print("Game Engine Started...! ⚡")
    time.sleep(1)
    print("CPU load exceeding...! 🔥")
    time.sleep(2)
    print("Starting RPS Game Engine - 17.3 GB 💾")
    print("Ready to play! 🎯✨")
    time.sleep(1)

    choices = ["rock", "paper", "scissors"]

    while True:
        user_input = input("\nEnter 'rock', 'paper', or 'scissors' (or 'quit' to exit): ").strip().lower()
        
        if user_input == "quit":
            print("Thanks for playing! Exiting Nvidia Engine... 👋✨")
            break
            
        if user_input not in choices:
            print("❌ Invalid move! Please choose 'rock', 'paper', or 'scissors' 🤦‍♂️")
            continue

        server_choice = random.choice(choices)
        print(f"🤖 Nvidia Server picked: {server_choice.upper()} 💥")

        if user_input == server_choice:
            print("🤝 It's a Tie! Great minds think alike! ⚡")
        elif (
            (user_input == "rock" and server_choice == "scissors") or
            (user_input == "paper" and server_choice == "rock") or
            (user_input == "scissors" and server_choice == "paper")
        ):
            print("🏆 You Win! You defeated the Nvidia AI Supercomputer! 🎉🥳")
        else:
            print("💀 You Lose! Better luck next time against the AI! 🤖🔥")

if __name__ == "__main__":
    play()
