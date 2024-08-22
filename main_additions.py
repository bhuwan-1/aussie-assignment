# Function to calculate the grade based on the total marks
def calculateGrade(marks):
    if marks >= 80:
        return "High Distinction"
    elif marks >= 70:
        return "Distinction"
    elif marks >= 60:
        return "Credit"
    elif marks >= 50:
        return "Pass"
    else:
        return "Fail"

# Main program with additional features
def main():
    # Prompt user for the number of assessments with input validation
    numAssessments = int(input("Enter the number of assessments: "))
    while numAssessments < 1:
        print("Number of assessments must be at least 1.")
        numAssessments = int(input("How many assessment? : "))

    # Initialize lists to store assessment names and their values
    assessmentNames = []
    assessmentValues = []

    # Loop to collect assessment names and values
    for i in range(numAssessments):
        assessmentName = input(f"Enter name of assessment {i+1}: ")
        assessmentNames.append(assessmentName)

        assessmentValue = input(f"Enter value of {assessmentName} out of 100: ")
        if assessmentValue == "":
            assessmentValue = 0
        else:
            assessmentValue = int(assessmentValue)
        while assessmentValue < 0 or assessmentValue > 100:
            print("Invalid value. Please enter a number between 0 and 100.")
            assessmentValue = int(input(f"Enter value of {assessmentName} out of 100: "))
        assessmentValues.append(assessmentValue)

    # Verify that the sum of all assessment values equals 100
    if sum(assessmentValues) != 100:
        print("The total value of assessments must equal 100. Please restart the program.")
        return

    # Prompt user for the number of students with input validation
    numStudents = int(input("Total students?: "))
    while numStudents < 1:
        print("Number of students must be at least 1.")
        numStudents = int(input("Total students?: "))

    # Initialize a list to store student details
    studentDetails = []

    # Loop to get student names and their corresponding marks
    for j in range(numStudents):
        studentName = input(f"\nEnter the name of student {j+1}: ")
        
        studentMarks = []
        totalMarks = 0
        
        for k in range(numAssessments):
            mark = input(f"Enter marks for {studentName} in {assessmentNames[k]} out of {assessmentValues[k]}: ")
            if mark == "":
                mark = 0
            else:
                mark = int(mark)
            while mark < 0 or mark > assessmentValues[k]:
                print(f"Invalid mark. Please enter a number between 0 and {assessmentValues[k]}.")
                mark = int(input(f"Enter marks for {studentName} in {assessmentNames[k]} out of {assessmentValues[k]}: "))
            studentMarks.append(mark)
            totalMarks += mark
            # Calculate grade for individual assessment
            grade = calculateGrade((mark / assessmentValues[k]) * 100)
            print(f"{mark} out of {assessmentValues[k]} is a {grade}")
        
        # Calculate the overall grade for the student based on the totalMarks
        finalGrade = calculateGrade(totalMarks)
        
        # Store student name, marks, total marks, and final grade in studentDetails
        studentDetails.append({
            "name": studentName,
            "marks": studentMarks,
            "totalMarks": round(totalMarks),
            "grade": finalGrade
        })
        
        print(f"{studentName} has a total marks of {round(totalMarks)} ({finalGrade})")

    print("\nAll marks entered!")
    
    # Calculate and print class average, top student details, and pass percentage
    classTotalMarks = 0
    topStudents = []
    topMarks = 0
    passCount = 0

    for student in studentDetails:
        classTotalMarks += student["totalMarks"]
        if student["totalMarks"] > topMarks:
            topMarks = student["totalMarks"]
            topStudents = [student["name"]]
        elif student["totalMarks"] == topMarks:
            topStudents.append(student["name"])

        if student["totalMarks"] >= 50:
            passCount += 1

    classAverage = round(classTotalMarks / numStudents)
    classAverageGrade = calculateGrade(classAverage)
    passPercentage = (passCount / numStudents) * 100

    print(f"The class average is {classAverage} ({classAverageGrade})")
    print(f"The top student is {', '.join(topStudents)} with a total mark of {topMarks}")
    print(f"Pass Percentage: {passCount}/{numStudents} students ({round(passPercentage)}%) passed the class")

if __name__ == "__main__":
    main()
