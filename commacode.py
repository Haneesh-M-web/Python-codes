def main():
    print("Comma Code Program")
    print("This program formats lists with proper comma separation.")
    
    while True:
        user_input = input("\nEnter items separated by commas (or 'quit' to exit): ").strip()
        
        if user_input.lower() == 'quit':
            print("Goodbye!")
            break
        
        if not user_input:
            print("Please enter at least one item.")
            continue
        
        # Split input into list, stripping whitespace
        items = [item.strip() for item in user_input.split(',')]
        
        # Remove empty strings if any
        items = [item for item in items if item]
        
        # Format and display the result
        formatted = comma_code(items)
        print("\nFormatted result:")
        print(formatted)

if _name_ == "_main_":
    main()