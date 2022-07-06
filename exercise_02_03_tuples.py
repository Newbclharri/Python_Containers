###############
## Exercise 02
###############
# Create a tuple named foodscontaining the same number of foods (strings) as there are names in the studentslist.
# Use a forloop to print out the string "food goes here is a good food".
foods = ("Crawfish", "Truffle", "Cauliflower", "Seaweed")

for food in foods:
    print(food + " is a good food.")

print("\n---------------------------------------------------------------\n")

#################
## Exercise 03
#################
# Using a forloop, print just the last two food strings from foods.

for i in range(1,3):
    print(foods[-(i)])