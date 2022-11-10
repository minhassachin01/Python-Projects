print("STUDENTS GRADES CALCULATOR\n")                       #Using escape to format output
print("Enter number of students: ")
i=int(input())
n=1
while n<= i :
    n=n+1
    print("Enter the student name: ")
    name=str(input())
    print("Enter student id: ")
    student_id=int(input())
    print("Total marks in Pyhton course: ")
    marks=int(input())
    print("-----Student Information----")
    print("Name:",name)
    print("Student Id:",student_id)
    print("Total Marks:",marks)
    if marks>=94 and marks<=100:
        print("Grade: A+")
        print("Grade point: 4.0")
        print("--Enter next Student information---")
    elif marks>=87 and marks<=93:
        print("Grade: A")
        print("Grade point: 3.7")
        print("--Enter next Student information---")
    elif marks>=80 and marks<=86:
        print("Grade: A-")
        print("Grade point: 3.5")
        print("--Enter next Student information---")
    elif marks>=77 and marks<=79:
        print("Grade: B+")
        print("Grade point: 3.2")
        print("--Enter next Student information---")
    elif marks>=73 and marks<=76:
        print("Grade: B")
        print("Grade point: 3.0")
        print("--Enter next Student information---")
    elif marks>=70 and marks<=72:
        print("Grade: B-")
        print("Grade point: 2.7")
        print("--Enter next Student information---")
    elif marks>=67 and marks<=69:
        print("Grade: C+")
        print("Grade point: 2.3")
        print("--Enter next Student information---")
    elif marks>=63 and marks<=66:
        print("Grade: C")
        print("Grade point: 2.0")
        print("--Enter next Student information---")
    elif marks>=60 and marks<=62:
        print("Grade: C-")
        print("Grade point: 1.7")
        print("--Enter next Student information---")
    elif marks>=50 and marks<=59:
        print("Grade: D")
        print("Grade point: 1.0")
        print("--Enter next Student information---")
    elif marks>=0 and marks<=49:
        print("Grade: F")
        print("Grade point: 0.0")
        print("--Enter next Student information---")
    else:
        print("Enter marks between 0 to 100")
