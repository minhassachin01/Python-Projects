print("STUDENTS GRADES CALCULATOR\n")                       #Using escape to format output
stu_name = input("Enter Student's Name: ")
stu_id = input("Enter Student ID: ")
py_marks = int(input("Enter Student's Marks in Python: "))  #Converting string to int for use in the code
py_grade = "NA"                     
py_grade_point = 0.0

if (py_marks > 100 or py_marks < 0):            #Raising a error message if the input marks is more than 100 or negative
    print("You have entered an Invalid Input, Please check your values & try again.")
else:
    if (py_marks >= 94 and py_marks <= 100):
        py_grade = "A+"
        py_grade_point = 4.0
    elif (py_marks >= 87 and py_marks <= 93):
        py_grade = "A"
        py_grade_point = 3.7
    elif (py_marks >= 80 and py_marks <= 86):
        py_grade = "A-"
        py_grade_point = 3.5
    elif (py_marks >= 77 and py_marks <= 79):
        py_grade = "B+"
        py_grade_point = 3.2
    elif (py_marks >= 73 and py_marks <= 76):
        py_grade = "B"
        py_grade_point = 3.0
    elif (py_marks >= 70 and py_marks <= 72):
        py_grade = "B-"
        py_grade_point = 2.7
    elif (py_marks >= 67 and py_marks <= 69):
        py_grade = "C+"
        py_grade_point = 2.3
    elif (py_marks >= 63 and py_marks <= 66):
        py_grade = "C"
        py_grade_point = 2.0
    elif (py_marks >= 60 and py_marks <= 62):
        py_grade = "C-"
        py_grade_point = 1.7
    elif (py_marks >= 50 and py_marks <= 59):
        py_grade = "D"
        py_grade_point = 1.0
    else:
        py_grade = "F"
        py_grade_point = 0.0

    print("\nYour Python Result is as Follows:-")       #printing students data
    print("Students Name: " + stu_name)
    print("Student ID: " + stu_id)
    print("Total Marks: " + str(py_marks))
    print("Grade: " + py_grade)
    print("Grade Point: " + str(py_grade_point))
    
        
