students = []

for i in range(3):
    print(f"\nStudent {i + 1}")
    student = {}

    student["name"] = input("Enter name: ")
    student["age"] = input("Enter age: ")
    student["grade"] = input("Enter grade: ")
    students.append(student)

print("\nClass Directory:")
for student in students:
    print(f"{student['name']} | Age: {student['age']} | Grade: {student['grade']}")
