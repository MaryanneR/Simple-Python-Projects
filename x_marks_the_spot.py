# Create lists
row1 = ["⬜","⬜","⬜"]
row2 = ["⬜","⬜","⬜"]
row3 = ["⬜","⬜","⬜"]
map = [row1, row2, row3]

# Print grid
print(f"{row1}\n{row2}\n{row3}")

# Get input
print("Where would you bury your treasure?")
print("Enter in format 'column row' e.g. column 1 row 2 would be 12.")
position = input("Which spot did you pick? :\n")

# Convert input into index values
column = int(position[0]) - 1
row = int(position[1]) - 1

# Change value in nested list
map[row][column] = "X"

# Print new map with X replacing desired value
print(f"{row1}\n{row2}\n{row3}")