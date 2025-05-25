def print_grid(grid):
    """Print the grid in its original orientation"""
    for row in grid:
        print(' '.join(row))

def rotate_grid_clockwise(grid):
    """Rotate the grid 90 degrees clockwise"""
    # Transpose the grid (swap rows and columns)
    transposed = list(zip(*grid))
    # Reverse each row to complete the rotation
    rotated = [list(reversed(row)) for row in transposed]
    return rotated

def main():
    # Sample character picture grid (heart shape)
    grid = [
        ['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']
    ]

    print("Original Grid:")
    print_grid(grid)

    while True:
        print("\nOptions:")
        print("1. Rotate 90° clockwise")
        print("2. Rotate 90° counter-clockwise")
        print("3. Flip horizontally")
        print("4. Flip vertically")
        print("5. Reset to original")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            grid = rotate_grid_clockwise(grid)
            print("\nRotated 90° clockwise:")
        elif choice == '2':
            # Rotating counter-clockwise is 3 clockwise rotations
            for _ in range(3):
                grid = rotate_grid_clockwise(grid)
            print("\nRotated 90° counter-clockwise:")
        elif choice == '3':
            grid = [list(reversed(row)) for row in grid]
            print("\nFlipped horizontally:")
        elif choice == '4':
            grid = list(reversed(grid))
            print("\nFlipped vertically:")
        elif choice == '5':
            grid = [
                ['.', '.', '.', '.', '.', '.'],
                ['.', 'O', 'O', '.', '.', '.'],
                ['O', 'O', 'O', 'O', '.', '.'],
                ['O', 'O', 'O', 'O', 'O', '.'],
                ['.', 'O', 'O', 'O', 'O', 'O'],
                ['O', 'O', 'O', 'O', 'O', '.'],
                ['O', 'O', 'O', 'O', '.', '.'],
                ['.', 'O', 'O', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.']
            ]
            print("\nReset to original:")
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
            continue

        print_grid(grid)

if _name_ == "_main_":
    main()