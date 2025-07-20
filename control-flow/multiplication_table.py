# This code creates a multiplication table

num1 = int(input("Enter a number to see its multiplication table: "))  # prompts user to enter number to get multiplication table.

for x in range(1,11):
    product = num1 * x
    print(f"{num1} * {x} = {product}", end="\t")