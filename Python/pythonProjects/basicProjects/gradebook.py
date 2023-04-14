# Returns the Letter Grade of the student
def letterGrade(gradeAverage):
    studentGrade = ""
    if gradeAverage >= 90:
        studentGrade = "A"
    elif gradeAverage >= 80:
        studentGrade = "B"
    elif gradeAverage >= 70:
        studentGrade = "C"
    elif gradeAverage >= 60:
        studentGrade = "D"
    else:
        studentGrade = "F"
    return studentGrade

# Gets the average of 3 grades
def gradeAvg(grade1, grade2, grade3):
    sum = grade1 + grade2 + grade3
    avg = sum/3
    return avg

# Gets information about a student then prints the first name, last name, grade avg, and letter grade
def main():
    fname = input("Student First Name:")
    lname = input("Student Last Name:")
    grade1 = int(input("Grade1: "))
    grade2 = int(input("Grade2: "))
    grade3 = int(input("Grade3: "))
    avg = round(gradeAvg(grade1, grade2, grade3), 0)
    letter = letterGrade(avg)

    print(f"Name: {fname} {lname}; Grades: {grade1}, {grade2}, {grade3}; Grade Average: {avg}; Letter Grade: {letter}")

main()