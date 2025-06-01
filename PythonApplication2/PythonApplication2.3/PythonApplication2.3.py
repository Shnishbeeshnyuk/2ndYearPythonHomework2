def find_common_elements():
    # Get first list of numbers
    list1 = input("Enter first list of numbers: ").split()
    
    # Get second list of numbers
    list2 = input("Enter second list of numbers: ").split()
    
    try:
        # Convert to sets of integers
        set1 = set(map(int, list1))
        set2 = set(map(int, list2))
        
        # Find intersection
        common = set1 & set2  # or set1.intersection(set2)
        
        # Convert back to sorted list for consistent output
        common_sorted = sorted(common)
        
        # Print result
        print("Common elements:", *common_sorted)
        
    except ValueError:
        print("Error: Please enter numbers only!")

# Run the program
find_common_elements()
