class Student:
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number
        self.marks = []

    def add_marks(self, subject, mark):
        self.marks.append((subject, mark))

    def calculate_average(self):
        if not self.marks:
            return 0.0
        total_marks = sum(mark for subject, mark in self.marks)
        return total_marks / len(self.marks)

# Create an instance of the Student class
student1 = Student("Omar Akbar Have ", "321321")

# Add marks for different subjects
student1.add_marks("Machine Learning", 70)
student1.add_marks("Digital System Design", 85)
student1.add_marks("Image Processing", 50)
student1.add_marks("IOT", 72)

# Calculate and print the average marks
average_marks = student1.calculate_average()
print(f"{student1.name}'s average marks: {average_marks}")
