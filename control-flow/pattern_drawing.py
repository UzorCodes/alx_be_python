# This code prints out a square pattern where the length and width is the number inputted by the user

length = int(input("Enter the size of the pattern: "))
i = 1

while i <= length: # Outer loop controls the number of rows
  for j in range(1, length + 1): # Inner loop prints asterisks for each row
    print("*", end="")
  print()
  i += 1