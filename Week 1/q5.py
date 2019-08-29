# Created by Amos Tan for students to reference their lab work
# Q5

# #################################
# The code below is given!!!!
# #################################
# You are given the following constants:

# Annual interest rate (which is fixed)
ANNUAL_INTEREST_RATE = 0.005
# Number of times the interest is compounded per year
FREQUENCY_OF_COMPOUNDING = 12

# #################################
# Write your code below:
# #################################

# Input
principal = float(input("What's the amount of your principal? "))
time = float(input("How many years do you want to deposit the money? "))

# Calculate 
newAmount = principal * (1 + ANNUAL_INTEREST_RATE/FREQUENCY_OF_COMPOUNDING) ** (FREQUENCY_OF_COMPOUNDING * time)
interest = newAmount - principal

# Print
print(f"The interest you will earn is ${round(interest, 2)}")

