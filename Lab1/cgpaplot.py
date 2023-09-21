current_cgpa = float(input("Enter your current CGPA: "))
total_credit_hours_studied = int(input("Enter the total credit hours studied: "))

current_semester_credit_hours = int(input("Enter current semester credit hours: "))
future_cgpa = float(input("Enter your desired future CGPA: "))


total_points = current_cgpa * total_credit_hours_studied

cpga = total_points / total_credit_hours_studied

print(cpga)