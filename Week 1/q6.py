# Created by Amos Tan for students to reference their lab work
# Q6

# Additional notes: 
# Could be improved with loops but the concept have yet be taught to students

# Additional Practice: 
# Rewrite the code using loops

# ################################
# The code below is given!!!!
# ################################

amount = float(input("Enter payment amount (US$) :"))
amount_in_cents = int(round(amount * 100))

# ################################
# Write your code below:
# ################################

twentyDollarNotes = amount_in_cents // 2000
amount_in_cents = amount_in_cents % 2000 

tenDollarNotes  = amount_in_cents // 1000
amount_in_cents = amount_in_cents % 1000

fiveDollarNotes = amount_in_cents // 500
amount_in_cents = amount_in_cents % 500

oneDollarNotes = amount_in_cents // 100
amount_in_cents = amount_in_cents % 100

quarterCoins = amount_in_cents // 25
amount_in_cents = amount_in_cents % 25

dimeCoins = amount_in_cents // 10
amount_in_cents = amount_in_cents % 10

nickleCoins = amount_in_cents // 5
amount_in_cents = amount_in_cents % 5

pennyCoins = amount_in_cents

# Print
print("You need to give:")
print(f"   {twentyDollarNotes} ($20 notes)")
print(f"   {tenDollarNotes} ($10 notes)")
print(f"   {fiveDollarNotes} ($5 notes)")
print(f"   {oneDollarNotes} ($1 notes)")
print(f"   {quarterCoins} (quarter coins)")
print(f"   {dimeCoins} (dime coins)")
print(f"   {nickleCoins} (nickle coins)")
print(f"   and {pennyCoins} (penny coins)")