size = int(input("Enter the size of the pattern:"))
row = 0
while row < size:
    for col in range(size):
        print("*", end="")
    print()
    row += 1
# The code above generates a square pattern of asterisks based on the user-defined size.