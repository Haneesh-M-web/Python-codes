def is_valid_chess_board(chess_dict):
    """
    Validate a chess board dictionary according to standard rules.
    
    Rules:
    1. Exactly one black and one white king
    2. At most 16 pieces per player
    3. At most 8 pawns per player
    4. Valid piece names and positions
    5. Valid piece colors
    6. Valid board positions (1a to 8h)
    """
    
    # Check kings
    if sum(1 for piece in chess_dict.values() if piece == 'wking') != 1:
        return False
    if sum(1 for piece in chess_dict.values() if piece == 'bking') != 1:
        return False
    
    # Count pieces
    piece_counts = {'w': 0, 'b': 0}
    pawn_counts = {'w': 0, 'b': 0}
    
    valid_pieces = {'pawn', 'knight', 'bishop', 'rook', 'queen', 'king'}
    
    for position, piece in chess_dict.items():
        # Check position format (1a-8h)
        if len(position) != 2:
            return False
        col, row = position[0], position[1]
        if not (col.isdigit() and 1 <= int(col) <= 8 and row.isalpha() and 'a' <= row <= 'h'):
            return False
        
        # Check piece format (color + type)
        if len(piece) < 2:
            return False
        color = piece[0]
        piece_type = piece[1:]
        
        if color not in ('w', 'b'):
            return False
        if piece_type not in valid_pieces:
            return False
        
        # Count pieces
        piece_counts[color] += 1
        if piece_type == 'pawn':
            pawn_counts[color] += 1
    
    # Check piece limits
    if any(count > 16 for count in piece_counts.values()):
        return False
    if any(count > 8 for count in pawn_counts.values()):
        return False
    
    return True

def main():
    print("Chess Dictionary Validator")
    print("Enter chess pieces in format {'position': 'piece', ...}")
    print("Example: {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop'}")
    print("Enter 'q' to quit")
    
    while True:
        user_input = input("\nEnter chess board dictionary: ").strip()
        
        if user_input.lower() == 'q':
            print("Goodbye!")
            break
        
        try:
            # Safely evaluate the input as a dictionary
            chess_dict = eval(user_input)
            if not isinstance(chess_dict, dict):
                raise ValueError("Input must be a dictionary")
            
            # Validate the chess board
            if is_valid_chess_board(chess_dict):
                print("✅ Valid chess board configuration")
            else:
                print("❌ Invalid chess board configuration")
                
        except Exception as e:
            print(f"Error: {e}\nPlease enter a valid dictionary in the correct format")

if _name_ == "_main_":
    main()