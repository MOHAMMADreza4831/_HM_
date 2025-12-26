students_list = [
    {
        "student_id": 1,
        "name": "ali",
        "grades": [20, 19, 20]
    },
    {
        "student_id": 2,
        "name": "mmd",
        "grades": [15, 14, 16.5]
    },
    {
        "student_id": 3,
        "name": "mehdi",
        "grades": [12, 13.5, 11 , 5]
    }
]

def calculate_student_gpa(student):
    grades = student["grades"]
    if not grades:   
        return 0
    return sum(grades) / len(grades)

for student in students_list:
    gpa = calculate_student_gpa(student)
    print(f"name = {student['name']}  moadel = {gpa:.2f}")
