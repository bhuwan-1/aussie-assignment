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

# Main program 
def main():
    # Prompt user for the number of assessments
    numAssessments = int(input("Enter the number of assessments: "))

    # Initialize lists to store assessment names and corresponding values
    assessmentNames = []
    assessmentValues = []

    # Loop that collects assessment names and values
    for i in range(numAssessments):
        assessmentName = input(f"Enter name of assessment {i+1}: ")
        assessmentNames.append(assessmentName)

        assessmentValue = int(input(f"Enter value of {assessmentName} out of 100: "))
        while assessmentValue < 0 or assessmentValue > 100:
            print("Invalid value. Please enter a number between 0 and 100.")
            assessmentValue = int(input(f"Enter value of {assessmentName} out of 100: "))
        assessmentValues.append(assessmentValue)

    # Verifying that the sum of all assessment values = 100
    if sum(assessmentValues) != 100:
        print("The total value of assessments must equal 100. Please restart the program.")
        return

    # Prompt user for the number of students
    numStudents = int(input("Total students?: "))

    # Initialize a list to store student details
    studentDetails = []

    # Loop to get student names and their corresponding marks
    for j in range(numStudents):
        studentName = input(f"\nEnter the name of student {j+1}: ")
        
        studentMarks = []
        totalMarks = 0
        
        for k in range(numAssessments):
            mark = int(input(f"Enter marks for {studentName} in {assessmentNames[k]} out of {assessmentValues[k]}: "))
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
    
    # Calculate and print class average and top student details
    classTotalMarks = 0
    topStudent = ""
    topMarks = 0

    for student in studentDetails:
        classTotalMarks += student["totalMarks"]
        if student["totalMarks"] > topMarks:
            topMarks = student["totalMarks"]
            topStudent = student["name"]

    classAverage = round(classTotalMarks / numStudents)
    classAverageGrade = calculateGrade(classAverage)
    print(f"The class average is {classAverage} ({classAverageGrade})")
    print(f"The top student is {topStudent} with a total mark of {topMarks}")

# ensures that the main function is executed when the code runs directly.
# it is not executed when the code is imported.
if __name__ == "__main__":
    main()
