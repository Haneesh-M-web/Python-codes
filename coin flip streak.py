import random

def flip_coin():
    """Simulate a single coin flip"""
    return random.choice(['H', 'T'])

def count_streaks(flips):
    """Count streaks in a sequence of coin flips"""
    if not flips:
        return 0
    
    streaks = 0
    current_streak = 1
    
    for i in range(1, len(flips)):
        if flips[i] == flips[i-1]:
            current_streak += 1
        else:
            if current_streak >= 6:  # Count as streak if 6 or more in a row
                streaks += 1
            current_streak = 1
    
    # Check the last streak
    if current_streak >= 6:
        streaks += 1
    
    return streaks

def simulate_flips(num_experiments=10000, num_flips=100):
    """Run multiple experiments to calculate probability of streaks"""
    streak_counts = []
    
    for _ in range(num_experiments):
        flips = [flip_coin() for _ in range(num_flips)]
        streaks = count_streaks(flips)
        streak_counts.append(streaks)
    
    probability = sum(1 for count in streak_counts if count >= 1) / num_experiments
    average_streaks = sum(streak_counts) / num_experiments
    
    return probability, average_streaks

def main():
    print("Coin Flip Streak Analyzer")
    print("This program calculates the probability of getting streaks of 6+ heads/tails in a row.")
    
    while True:
        try:
            num_flips = int(input("\nEnter number of flips per experiment (100-10000): "))
            num_experiments = int(input("Enter number of experiments to run (100-10000): "))
            
            if num_flips < 100 or num_experiments < 100:
                print("Minimum values are 100. Try again.")
                continue
            
            print("\nRunning simulation...")
            probability, average = simulate_flips(num_experiments, num_flips)
            
            print(f"\nResults from {num_experiments:,} experiments of {num_flips:,} flips each:")
            print(f"Probability of at least one streak: {probability:.2%}")
            print(f"Average number of streaks per experiment: {average:.2f}")
            
            if input("\nRun another simulation? (y/n): ").lower() != 'y':
                print("Goodbye!")
                break
                
        except ValueError:
            print("Please enter valid integers.")

if _name_ == "_main_":
    main()