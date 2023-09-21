student_records = {}

def create_student_record(registration_number, name, email, gender):
    if registration_number not in student_records:
        student_records[registration_number] = {'Name': name, 'Email': email, 'Gender': gender}
        print(f"Student record for registration number {registration_number} created successfully.")
    else:
        print(f"Registration number {registration_number} already exists.")

def delete_student_record(registration_number):
    if registration_number in student_records:
        del student_records[registration_number]
        print(f"Student record for registration number {registration_number} deleted successfully.")
    else:
        print(f"Registration number {registration_number} does not exist.")

def modify_student_record(registration_number, name=None, email=None, gender=None):
    if registration_number in student_records:
        student = student_records[registration_number]
        if name is not None:
            student['Name'] = name
        if email is not None:
            student['Email'] = email
        if gender is not None:
            student['Gender'] = gender
        print(f"Student record for registration number {registration_number} modified successfully.")
    else:
        print(f"Registration number {registration_number} does not exist.")

while True:
    print("1. Create Student Record")
    print("2. Delete Student Record")
    print("3. Modify Student Record")
    choice = input("Select an option (1/2/3): ")
 


    if choice == '1':
        registration_number = input("Enter Registration Number: ")
        name = input("Enter Name: ")
        email = input("Enter Email: ")
        gender = input("Enter Gender: ")
        create_student_record(registration_number, name, email, gender)
    elif choice == '2':
        registration_number = input("Enter Registration Number to delete: ")
        delete_student_record(registration_number)
    elif choice == '3':
        registration_number = input("Enter Registration Number to modify: ")
        name = input("Enter new Name (press Enter to skip): ")
        email = input("Enter new Email (press Enter to skip): ")
        gender = input("Enter new Gender (press Enter to skip): ")
        modify_student_record(registration_number, name, email, gender)
    
    else:
        print("Invalid selection.")