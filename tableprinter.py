def print_table(table_data):
    # Find the maximum width of each column
    col_widths = [max(len(str(item)) for item in col) for col in zip(*table_data)]

    # Print each row with formatted columns
    for row in table_data:
        formatted_row = " | ".join(str(item).ljust(width) for item, width in zip(row, col_widths))
        print(formatted_row)

# Example data
data = [
    ["Name", "Age", "City"],
    ["Alice", 30, "New York"],
    ["Bob", 24, "Los Angeles"],
    ["Charlie", 29, "Chicago"]
]

# Print the table
print_table(data)
