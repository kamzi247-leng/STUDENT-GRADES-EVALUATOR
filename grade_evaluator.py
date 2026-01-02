# This is a simple grade evaluator for students
name = input("Enter Student name: ")
course_name = input("Enter Course name: ")
score = float(input("Enter Student score(0-100): "))
print(" ")

print(f"Student Name: {name}")
print(f"Course Name: {course_name}")

if score >= 70:
    print("Grade: A")
elif 60 <= score < 69:
    print("Grade: B")
elif 50 <= score < 59:
    print("Grade: C")
elif 40 <= score < 49:
    print("Grade: D")
elif 30 <= score < 39:
    print("Grade: E")
else:
    print("Grade: F")

    #This is the Nigerian Federal University of Technology, Owerri grading system.
