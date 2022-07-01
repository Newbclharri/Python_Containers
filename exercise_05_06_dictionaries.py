####################
## VARIABLES
####################
students = ["Calvin Harris", "Mark Harris", "William Wise", "Madhu Sanjeev"]
foods = ("Crawfish", "Truffle", "Cauliflower", "Seaweed")

###############
## Exercise 05
###############

home_town = {
    "city": "Arcadia",
    "state": "California",
    "population": 58000
}

for key, val in home_town.items():
    print(f"{key} = {val}")

print("\n---------------------------------------------------------------\n")

###############
## Exercise 06
###############

cohort = []

for i in range(len(students)):
    cohort.append({
        "student": students[i],
        "fave_food": foods[i]
    })
    
for student in cohort:
    print(student)
