def collatz_sequence(n):
    """Generate the Collatz sequence for a given starting number"""
    sequence = [n]
    while n != 1:
        if n % 2 == 0:  # Even number
            n = n // 2
        else:            # Odd number
            n = 3 * n + 1
        sequence.append(n)
    return sequence

def analyze_collatz(start, end):
    """Analyze Collatz sequences for numbers in a range"""
    results = []
    for num in range(start, end + 1):
        seq = collatz_sequence(num)
        results.append({
            'number': num,
            'sequence': seq,
            'length': len(seq),
            'max_value': max(seq)
        })
    return results

def main():
    print("Collatz Sequence Generator")
    while True:
        try:
            num = int(input("\nEnter a positive integer (or 0 to quit): "))
            if num == 0:
                print("Goodbye!")
                break
            if num < 1:
                print("Please enter a positive integer.")
                continue
            
            seq = collatz_sequence(num)
            print(f"\nCollatz sequence for {num}:")
            print(" -> ".join(map(str, seq)))
            print(f"Length: {len(seq)} steps")
            print(f"Maximum value: {max(seq)}")
            
            # Optional: Show analysis for a range
            if len(seq) > 20 and input("\nShow analysis for numbers 1-10? (y/n): ").lower() == 'y':
                analysis = analyze_collatz(1, 10)
                print("\nAnalysis for numbers 1-10:")
                for result in analysis:
                    print(f"{result['number']}: {result['length']} steps, max {result['max_value']}")
                
        except ValueError:
            print("Please enter a valid integer.")

if _name_ == "_main_":
    main()