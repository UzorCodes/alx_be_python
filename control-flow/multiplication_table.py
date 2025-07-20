# This code creates a multiplication table

number = int(input("Enter a number to see its multiplication table: "))  # prompts user to enter number to get multiplication table.

for x in range(1,11):
    product = number * x
    print(f"{number} * {x} = {product}", end="\t")