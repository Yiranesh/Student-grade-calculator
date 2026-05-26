#==========================
# Student Grade Calculator
# by Yiranesh
# language: python
#==========================
 
# Determining the grade based on the mark
def grade_mark(mark):
    if mark >= 90:
        return "A+"
    elif mark >= 80:
        return "A "
    elif mark >= 75:
        return "A-"
    elif mark >= 70:
        return "B+"
    elif mark >= 65:
        return "B "
    elif mark >= 60:
        return "B-"
    elif mark >= 55:
        return "C+"
    elif mark >= 50:
        return "C "
    elif mark >= 45:
        return "C-"
    elif mark >= 40:
        return "D "
    else:
        return "F "
    
# Determining the GPA from the grade
def gpa_grade(grade):
    gpa_table = {"A+":4.00, "A ": 4.00, "A-": 3.7,
                 "B+": 3.3, "B ": 3.0, "B-": 2.7, 
                 "C+": 2.3, "C ": 2.0, "C-": 1.7, 
                 "D ": 1.0, "F ": 0.0 }
    return gpa_table.get(grade, 0.0)

# Calculate the CGPA from list of subjects
def calculate_cgpa(subjects):
    total_gpa = sum(gpa_grade(grade_mark(mark)) for subject, mark in subjects)
    return (total_gpa/len(subjects))
    
# Display the result table
def display_results(name, subjects):
    print("\n" + "="* 50)
    print(f"RESULT SLIP - {name.upper()}")
    print("="* 50)
    print(f"{'Subject':<25} {'Mark':>5}  {'Grade':>5} {'GPA':>5}")
    print("-" * 50)

    for subject, mark in subjects:
        grade = grade_mark(mark)
        gpa = gpa_grade(grade)
        print(f"{subject.capitalize():<25} {mark:>5.1f} {grade:>5}   {gpa:>5.2f}")

    cgpa = calculate_cgpa(subjects)
    
    print("-" * 50)
    print(f" {'CGPA:':>39}{cgpa:>5.2f} ")
    print("=" * 50)

# Determining the status
    if cgpa >= 3.5:
        status = "Dean's List"
    elif cgpa>= 2.0:
        status ="Pass"
    else:
        status = "Fail"
    
    print(f"Status : {status}")
    print("=" * 50)

def main():
    print("\n"+ "-" * 50)
    print("====Welcome to the Student Grade Calculator====")
    print("-" * 50)

    # Getting students name
    name = input("\nEnter your name: ")
    print(f"Welcome, {name.capitalize()}")

    if not name :
        name = "Student"

    # Getting the number of subjects
    while True:
        try:
            num_subject = int(input("\nEnter number of subject: "))

            if num_subject < 1:
                print("Number of subject cannot be less 1.")

            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number")
    
    #Getting the subjects name and marks
    subjects = []

    print()

    for x in range(num_subject):
        subject = input(f" Enter subject {x+1} name: ")

        if not subject:
            subject = f"Subject {x+1}"
    

        while True:
            try:
                mark = float(input(f" Enter your mark for {subject} (0-100): "))
                if mark < 0 or mark > 100:
                    print("Mark must be between 0 and 100")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a number")
        
        subjects.append((subject, mark))

    # Displays the result
    display_results(name, subjects)   

    # Ask to calculate for another student
    again = input("\nCalculate for a another student? (Y or N): ") 

    if again.lower() in ('y', 'yes'):
        main()           
    else:
        print("\n===Thank you for using the Student Grade Calculator===")
        print()


if __name__ == "__main__":
    main()
























































































































