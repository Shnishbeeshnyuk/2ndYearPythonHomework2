def process_numbers():
    # Get numbers from user
    numbers_input = input("Enter numbers separated by spaces: ").split()
    
    # Get power from user
    try:
        power = int(input("Enter power: "))
    except ValueError:
        print("Error: Power must be an integer!")
        return
    
    processed_list = []
    
    for item in numbers_input:
        try:
            # Try to convert to number
            num = float(item)
            # Handle negative numbers properly
            if num < 0 and power % 1 != 0:
                print(f"Cannot raise negative number {num} to fractional power")
                processed_list.append("NaN")
            else:
                result = num ** power
                # Convert to int if whole number for cleaner output
                if result.is_integer():
                    result = int(result)
                processed_list.append(str(result))
        except ValueError:
            # Handle string case
            processed_list.append(item * power)
    
    # Print the results
    print("Output:", " ".join(processed_list))

# Run the program
process_numbers()
