dct = {1: 11, 2: 22, 3: 33, 4: 4, 5: 33, 6: 1}

# Create sets for keys and values
keys_set = set(dct.keys())
values_set = set(dct.values())

# Combine the sets
combined_set = keys_set.union(values_set)

# Print the results
print("Keys set:", keys_set)
print("Values set:", values_set)
print("Combined set:", combined_set)
