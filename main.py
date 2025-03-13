import random

def main():
    play_again = True
    total_games = 0
    total_attempts = 0
    best_score = float('inf')
    
    while play_again:
        num = random.randint(0, 10)
        attempts = 0
        is_correct = False
        
        print("\nWelcome to the Number Guessing Game!")
        print("Try to guess the number between 0 and 10.")
        
        while not is_correct:
            guess = input("Enter a number between 0 and 10: ")
            guess = convert_input(guess)
            
            if isinstance(guess, int) and 0 <= guess <= 10:
                attempts += 1
                if guess == num:
                    print(f"\nCongratulations! {guess} is correct!")
                    print(f"It took you {attempts} attempts.")
                    is_correct = True
                    total_games += 1
                    total_attempts += attempts
                    best_score = min(best_score, attempts)
                elif guess > num:
                    print("Too high! Try again.")
                elif guess < num:
                    print("Too low! Try again.")
            else:
                print("Invalid input. Please enter a number between 0 and 10.")
        
        print_game_stats(total_games, total_attempts, best_score)
        play_again = ask_play_again()
    
    print("Thanks for playing!")

def convert_input(user_input):
    """Converts user input to an integer if valid, otherwise returns None."""
    try:
        return int(user_input)
    except ValueError:
        return None

def ask_play_again():
    """Asks the player if they want to play again and returns True or False."""
    while True:
        choice = input("Do you want to play again? (yes/no): ").strip().lower()
        if choice in ['yes', 'y']:
            return True
        elif choice in ['no', 'n']:
            return False
        else:
            print("Please enter 'yes' or 'no'.")

def print_game_stats(total_games, total_attempts, best_score):
    """Displays the player's game statistics."""
    print("\nGame Stats:")
    print(f"Total Games Played: {total_games}")
    print(f"Total Attempts: {total_attempts}")
    print(f"Average Attempts per Game: {total_attempts / total_games:.2f}" if total_games > 0 else "No games played yet.")
    print(f"Best Score (Fewest Attempts in a Game): {best_score}" if best_score != float('inf') else "No best score yet.")

if __name__ == "__main__":
    main()
