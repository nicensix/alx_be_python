import random

# Generate a list of random numbers between 1 and 10
random_numbers = [random.randint(1, 10) for _ in range(10)]

# Convert the list to a set to remove duplicates
unique_numbers = set(random_numbers)

# Print the unique numbers
print("Generated numbers:", random_numbers)
print("Unique numbers:", unique_numbers)