rows = 5  # Define pyramid height
i = 1  # Start outer loop

while i <= rows:
    # Print leading spaces
    j = 1
    while j <= (rows - i):
        print(" ", end="")
        j += 1

    # Print asterisks
    k = 1
    while k <= (2 * i - 1):
        print("*", end="")
        k += 1

    print()  # Move to the next row
    i += 1  # Increase row count