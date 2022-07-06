students = ["Calvin Harris", "Mark Harris", "William Wise", "Madhu Sanjeev"]
foods = ("Crawfish", "Truffle", "Cauliflower", "Seaweed")

###############
## Exercise 07
###############
# Using the list of studentsand list comprehension, assign to a variable named awesome_studentsa new list containing strings similar to this:
# ["Tina is awesome!", "Fred is awesome!", "Wilma is awesome!"]
# Iterate over awesome_studentsprinting out each string.

awesome_students = [student + " is awesome!" for student in students]

for student in awesome_students:
    print(student)

print("\n---------------------------------------------------------------\n")
    
###############
## Exercise 08
###############
# Using the tuple foods and list comprehension within a forloop, print each food string that contains the letter a.
# foods_with_a = [food for food in foods if "a" in food]

for food in foods_with_a:
    print(food)