import random
import time

class NumberGuessingGame:
    def __init__(self):
        self.high_scores = {'Easy': None, 'Medium': None, 'Hard': None}
        self.difficulty_settings = {
            '1': {'name': 'Easy', 'chances': 10},
            '2': {'name': 'Medium', 'chances': 5},
            '3': {'name': 'Hard', 'chances': 3}
        }
        
    def display_welcome(self):
        print("\n" + "="*50)
        print("Welcome to the Number Guessing Game!")
        print("I'm thinking of a number between 1 and 100.")
        print("="*50)
        
    def display_rules(self):
        print("\nRules:")
        print("1. I'll pick a random number between 1 and 100.")
        print("2. You need to guess the number within limited chances.")
        print("3. After each wrong guess, I'll tell you if the number is higher or lower.")
        print("4. Try to guess in as few attempts as possible!")
        print("-"*50)
        
    def get_difficulty(self):
        print("\nPlease select the difficulty level:")
        print("1. Easy (10 chances)")
        print("2. Medium (5 chances)")
        print("3. Hard (3 chances)")
        
        while True:
            choice = input("Enter your choice (1-3): ").strip()
            if choice in self.difficulty_settings:
                difficulty = self.difficulty_settings[choice]
                print(f"\nGreat! You have selected the {difficulty['name']} difficulty level.")
                print(f"You have {difficulty['chances']} chances to guess the number.")
                return difficulty
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
    
    def provide_hint(self, number, attempt, max_attempts):
        """Provide hints based on the user's progress"""
        if attempt == max_attempts // 2:
            if number % 2 == 0:
                print("! Hint: The number is even.")
            else:
                print("! Hint: The number is odd.")
        elif attempt >= max_attempts * 0.75:
            if number < 50:
                print("! Hint: The number is less than 50.")
            else:
                print("! Hint: The number is 50 or greater.")
    
    def play_round(self, difficulty):
        number = random.randint(1, 100)
        max_attempts = difficulty['chances']
        attempts = 0
        start_time = time.time()
        
        print("\n" + "="*50)
        print("Let's start the game!")
        print("="*50)
        
        while attempts < max_attempts:
            attempts_left = max_attempts - attempts
            print(f"\nYou have {attempts_left} chance{'s' if attempts_left > 1 else ''} left.")
            
            try:
                guess = int(input("Enter your guess (1-100): "))
                
                if guess < 1 or guess > 100:
                    print("Please enter a number between 1 and 100.")
                    continue
                    
                attempts += 1
                
                if guess == number:
                    end_time = time.time()
                    time_taken = end_time - start_time
                    print(f"\n🎉 Congratulations! You guessed the correct number in {attempts} attempt{'s' if attempts > 1 else ''}!")
                    print(f"⏱️ Time taken: {time_taken:.2f} seconds")
                    
                    # Update high score
                    self.update_high_score(difficulty['name'], attempts)
                    return True, attempts, time_taken
                    
                elif guess < number:
                    print(f"Incorrect! The number is greater than {guess}.")
                else:
                    print(f"Incorrect! The number is less than {guess}.")
                
                # Provide hints
                self.provide_hint(number, attempts, max_attempts)
                
            except ValueError:
                print("Please enter a valid number!")
        
        print(f"\n💀 Game Over! You've run out of chances.")
        print(f"The number was: {number}")
        return False, attempts, time.time() - start_time
    
    def update_high_score(self, difficulty_name, attempts):
        if self.high_scores[difficulty_name] is None or attempts < self.high_scores[difficulty_name]:
            self.high_scores[difficulty_name] = attempts
            print(f"🏆 New high score for {difficulty_name} difficulty: {attempts} attempts!")
    
    def display_high_scores(self):
        print("\n" + "="*50)
        print("HIGH SCORES")
        print("="*50)
        for difficulty, score in self.high_scores.items():
            if score:
                print(f"{difficulty}: {score} attempts")
            else:
                print(f"{difficulty}: No score yet")
    
    def play_game(self):
        self.display_welcome()
        self.display_rules()
        
        total_rounds = 0
        total_wins = 0
        
        while True:
            difficulty = self.get_difficulty()
            won, attempts, time_taken = self.play_round(difficulty)
            
            total_rounds += 1
            if won:
                total_wins += 1
            
            # Display statistics
            print(f"\n📊 Round Statistics:")
            print(f"Rounds played: {total_rounds}")
            print(f"Wins: {total_wins}")
            print(f"Win rate: {(total_wins/total_rounds)*100:.1f}%")
            
            self.display_high_scores()
            
            # Ask to play again
            play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
            if play_again not in ['yes', 'y']:
                print("\n" + "="*50)
                print("Thank you for playing the Number Guessing Game!")
                print("="*50)
                break

def main():
    game = NumberGuessingGame()
    game.play_game()

if __name__ == "__main__":
    main()