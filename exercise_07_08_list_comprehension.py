students = ["Calvin Harris", "Mark Harris", "William Wise", "Madhu Sanjeev"]
foods = ("Crawfish", "Truffle", "Cauliflower", "Seaweed")

###############
## Exercise 07
###############

awesome_students = [student + " is awesome!" for student in students]

for student in awesome_students:
    print(student)

print("\n---------------------------------------------------------------\n")
    
###############
## Exercise 08
###############

foods_with_a = [food for food in foods if "a" in food]

for food in foods_with_a:
    print(food)