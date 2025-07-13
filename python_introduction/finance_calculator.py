# This code calculates a user's monthly saving and an expected compound interest in a year
# The current year is assumed to be 2023 and the future year is 2050
 
monthly_income = int(input("Enter your monthly income: ")) # prompts user to enter monthly income
monthly_expenses = int(input("Enter your total monthly expense: ")) # prompts user to enter total monthly expense


#Calculates monthly savings
monthly_savings = monthly_income - monthly_expenses


#calculates compound interest in a year at an assumed rate of 5% per annum
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

# Outputs result of the calculation
print("Your monthly savings is $", monthly_savings)
print("Projected savings after one year, with interest, is: $", projected_savings)