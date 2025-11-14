students = int(input("Enter number of students: "))
subj = int(input("Enter number of subjects: "))

total_class_avrg = 0


for i in range(1, students + 1):
    print(f"\nStudent {i}")
    all_scores = 0
    
    for j in range(1, subj + 1):
        scores = float(input(f"Enter score {j}: "))
        all_scores += scores
    
    student_avrg = all_scores / subj
    print(f"Average for Student {i} = {student_avrg:.1f}")

    
    total_class_avrg += student_avrg


class_avrg = total_class_avrg / students
print(f"\nClass Average = {class_avrg:.1f}")