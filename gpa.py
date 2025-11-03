number_of_classes = int(input("How many classes are you in?"))
# Creates empty list to store the user's grades
grades = []
# Loops through each class to collect grades
for i in range(number_of_classes):
    while True:
        try:
            # Asks user to enter their grade as a float between 0 and 4
            grade = (float(input(f"Enter your grade for class {i+1} (0.0-4.0):")))
            # Validates that the grade is within the correct range
            if 0 <= grade <= 4:
                grades.append(grade)
                break
            else:
                print("Please enter a valid grade between 0.0 and 4.0.")
        except ValueError:
            # Handles non numeric inputs
            print("Invalid input. Please enter a number.")

# Calculates overall GPA by taking the average of all grades
gpa = sum(grades) / len(grades)

# Gives the user feedback based on their GPA
if gpa >= 3.0:
    print(f"Wow! Your grade point average is {gpa:.1f}, keep working hard!")
else:
    print(f"Oh! Your gpa is {gpa:.1f}, better luck next semester I guess..")

# If the user is taking more than 2 classes, allow semester GPA calculation
if number_of_classes >= 2:
    # Asks the user which semester's grades they want to analyze
    choice = input("Do you want to see your gpa for\n1:The first semester\n2:The second semester")
    # Splits semesters and selects grades based on the user's choice
    half = number_of_classes // 2
    if choice == "1":
        semester_grades = grades[:half]
    elif choice == "2":
        semester_grades = grades[half:]
    else:    
        print("Invalid input. Defaulting to first semester.")
        semester_grades = grades[:half]

    # Calculates GPA for chosen semester
    semester_gpa = sum(semester_grades) / len(semester_grades)
    print(f"Your gpa for this semester is {semester_gpa:.1f}")

    # Compares semester GPA to overall GPA and gives feedback
    if semester_gpa > gpa:
        print("Congrats! You improved this semester.")
    elif semester_gpa < gpa:
        print("Oh.. you didnt do as well this semester. Try harder next time!")
    else:
        print("Your grades stayed consistent.")
else:
    print("Not enough classes for semester analysis.")

# Asks user for their goal GPA
goal_gpa = float(input("Enter your goal gpa (0.0-4.0)"))
if not (0.0 <= goal_gpa <= 4.0):
    print("Invalid goal gpa. Must be between 0.0 and 4.0.")
else:
    #If user already met or exceeded goal GPA
    if goal_gpa <= gpa:
        print("Congrats! You've already met your goal gpa!")
    else:
            # Try raising one class grade to 4.0 to see if GPA goal can be met
            possible = False
            for i in range(len(grades)):
                temp_grades = grades.copy()
                temp_grades[i] = 4.0
                new_gpa = sum(temp_grades) / len(temp_grades)
                if new_gpa >= goal_gpa:
                    # If new GPA meets or exceeds goal, show how
                    print(f"\nIf you raise grade {i+1} to a 4.0, your new GPA would be {new_gpa:.2f}. Goal achieved!")
                    possible = True
            # If no single grade improvement reaches the goal, tell the user
            if not possible:
                print("\nYou’ll need to improve more than one grade to reach your goal GPA.")