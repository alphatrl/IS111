# Created by Amos Tan for students to reference their lab work
# Q3

# Constants
MERCURY_RATIO = 0.38
VENUS_RATIO = 0.91
JUPYTER_RATIO = 2.24

# Get mass
weight = float(input("What is your weight (in kg): "))

# convert to other planet weight
mercuryWeight = weight * MERCURY_RATIO
venusWeight = weight * VENUS_RATIO
juypterWeight = weight * JUPYTER_RATIO

# print
print(f"Mercury Weight: {mercuryWeight}kg")
print(f"Venus Weight: {venusWeight}kg")
print(f"Jupyter Weight: {juypterWeight}kg")
