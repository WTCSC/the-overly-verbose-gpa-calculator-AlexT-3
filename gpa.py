number_of_classes = int(input("How many classes are you in?"))
grades = []
for i in range(number_of_classes):
    while True:
        try:
            grade = (float(input(f"Enter your grade for class {i+1} (0.0-4.0):")))
            if 0 <= grade <= 4:
                grades.append(grade)
                break
            else:
                print("Please enter a valid grade between 0.0 and 4.0.")
        except ValueError:
            print("Invalid input. Please enter a number.")

gpa = sum(grades) / len(grades)

if gpa >= 3.0:
    print(f"Wow! Your grade point average is {gpa:.1f}, keep working hard!")
else:
    print(f"Oh! Your gpa is {gpa:.1f}, better luck next semester I guess..")

if number_of_classes >= 2:
    choice = input("Do you want to see your gpa for\n1:The first semester\n2:The second semester")
    half = number_of_classes // 2

    if choice == "1":
        semester_grades = grades[:half]
    elif choice == "2":
        semester_grades = grades[half:]
    else:    
        print("Invalid input. Defaulting to first semester.")
        semester_grades = grades[:half]

    semester_gpa = sum(semester_grades) / len(semester_grades)
    print(f"Your gpa for this semester is {semester_gpa:.1f}")

    if semester_gpa > gpa:
        print("Congrats! You improved this semester.")
    elif semester_gpa < gpa:
        print("Oh.. you didnt do as well this semester. Try harder next time!")
    else:
        print("Your grades stayed consistent.")
else:
    print("Not enough classes for semester analysis.")

goal_gpa = float(input("Enter your goal gpa (0.0-4.0)"))
if not (0.0 <= goal_gpa <= 4.0):
    print("Invalid goal gpa. Must be between 0.0 and 4.0.")
else:
    if goal_gpa <= gpa:
        print("Congrats! You've already met your goal gpa!")
    else:
            possible = False
            for i in range(len(grades)):
                temp_grades = grades.copy()
                temp_grades[i] = 4.0
                new_gpa = sum(temp_grades) / len(temp_grades)
                if new_gpa >= goal_gpa:
                    print(f"\nIf you raise grade {i+1} to a 4.0, your new GPA would be {new_gpa:.2f}. Goal achieved!")
                    possible = True

            if not possible:
                print("\nYou’ll need to improve more than one grade to reach your goal GPA.")
