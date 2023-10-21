def calculate_gpa(students):
    grading_scale = {
        (85, 100): ('A', 4.00),
        (80, 84): ('A-', 3.66),
        (75, 79): ('B+', 3.33),
        (71, 74): ('B', 3.00),
        (68, 70): ('B-', 2.66),
        (64, 67): ('C+', 2.33),
        (61, 63): ('C', 2.00),
        (58, 60): ('C-', 1.66),
        (54, 57): ('D+', 1.30),
        (50, 53): ('D', 1.00),
        (0, 49): ('F', 0.00),
    }

    result = []

    for student in students:
        name = student['name']
        marks = student['marks']
        total_grade_points = 0
        grades = []

        for mark in marks:
            for score_range, (grade, grade_point) in grading_scale.items():
                if score_range[0] <= mark <= score_range[1]:
                    total_grade_points += grade_point
                    grades.append(grade)
                    break

        gpa = total_grade_points / len(marks)

        student_info = {
            'name': name,
            'grades': grades,
            'grade_points': total_grade_points,
            'gpa': round(gpa, 2)
        }

        result.append(student_info)

    return result

# Example usage:
students = [
    {'name': 'Alice', 'marks': [92, 78, 85, 73, 88]},
    {'name': 'Bob', 'marks': [68, 75, 62, 58, 70]},
    {'name': 'Charlie', 'marks': [95, 88, 79, 87, 91]},
]

gpa_results = calculate_gpa(students)
for student in gpa_results:
    print(f"Name: {student['name']}, GPA: {student['gpa']}, Grades: {', '.join(student['grades'])}")