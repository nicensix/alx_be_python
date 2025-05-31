number = int(input("Enter a number to see its multiplication table: "))
for i in range(1, 11):
    result = number * i
    print(f"{result} x {i} = {result}")

# The code above is a simple multiplication table generator.
# It prompts the user to enter a number and then prints the multiplication table for that number from 1 to 10.