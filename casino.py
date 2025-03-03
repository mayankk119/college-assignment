import random
import time

# Function to simulate the slot machine game
def slot_machine():
    symbols = ['🍒', '🍀', '🍋', '🍉', '🍊']
    print("\n--- Welcome to the Slot Machine! ---")
    time.sleep(1)
    
    # Spin the slot machine
    spin = [random.choice(symbols) for _ in range(3)]
    print("Spinning... ", spin)
    time.sleep(1)
    
    if spin[0] == spin[1] == spin[2]:
        print("You win! Jackpot! 🎉")
        return True
    else:
        print("Better luck next time! 😞")
        return False

# Function to simulate the dice roll betting game
def dice_roll_betting():
    print("\n--- Welcome to Dice Roll Betting! ---")
    time.sleep(1)
    
    bet_amount = int(input("Enter your bet amount: $"))
    guess = int(input("Guess the dice roll (1-6): "))
    
    if guess < 1 or guess > 6:
        print("Invalid guess! Please choose a number between 1 and 6.")
        return
    
    print(f"You bet ${bet_amount} on the number {guess}. Rolling the dice...")
    time.sleep(2)
    
    roll = random.randint(1, 6)
    print(f"The dice rolled: {roll}")
    
    if guess == roll:
        winnings = bet_amount * 6  # You win 6x your bet if you guess correctly
        print(f"Congratulations! You win ${winnings}!")
    else:
        print(f"Sorry, you lost your bet of ${bet_amount}. Better luck next time!")
    
# Main function to control the casino games
def casino():
    print("Welcome to the Python Casino!")
    balance = 100  # Starting balance for the player
    
    while True:
        print("\nYour current balance is: $", balance)
        print("\n--- Choose a game to play ---")
        print("1. Slot Machine")
        print("2. Dice Roll Betting")
        print("3. Exit Casino")
        
        choice = input("Enter the number of the game you want to play: ")
        
        if choice == '1':
            if balance < 10:
                print("You don't have enough balance to play the Slot Machine.")
                continue
            balance -= 10  # Slot Machine costs $10 to play
            if slot_machine():
                balance += 50  # Jackpot win adds $50
        elif choice == '2':
            if balance < 5:
                print("You don't have enough balance to bet on the Dice Roll.")
                continue
            balance -= 5  # Dice Roll Betting costs $5 to play
            dice_roll_betting()
        elif choice == '3':
            print("Thanks for playing! Exiting Casino...")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
            
        if balance <= 0:
            print("You ran out of money! Game over.")
            break

# Start the casino game
if __name__ == "__main__":
    casino()
