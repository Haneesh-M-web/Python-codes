def zigzag_pattern(rows, cols):
    for i in range(rows):
        for j in range(cols):
            # Calculate when to print the asterisk
            if (i + j) % (2 * (rows - 1)) == 0 or (j - i) % (2 * (rows - 1)) == 0:
                print("*", end="")
            else:
                print(" ", end="")
        print()

# Example usage
zigzag_pattern(5, 30)
               
            