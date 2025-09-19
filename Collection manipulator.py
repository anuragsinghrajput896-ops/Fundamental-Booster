
students = []   

while True:
    print("===== Student Data Organizer =====")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")

    choice = input("Enter your choice: ")

    match choice:
        case "1":
            print("\nEnter student details:")
            student_id = input("Student ID: ")
            name = input("Name: ")
            age = input("Age: ")
            grade = input("Grade: ")
            dob = input("Date of Birth (YYYY-MM-DD): ")
            subjects = input("Subjects (comma-separated): ").split(",")

            student = {
                "ID": student_id,
                "Name": name,
                "Age": age,
                "Grade": grade,
                "DOB": dob,
                "Subjects": [s.strip() for s in subjects]
            }

            students.append(student)
            print("\nStudent added successfully!\n")

        case "2":
            if not students:
                print("\nNo students found!\n")
            else:
                print("\n--- Display All Students ---")
                for s in students:
                    print(f"Student ID: {s['ID']} | Name: {s['Name']} | Age: {s['Age']} | Grade: {s['Grade']} | DOB: {s['DOB']} | Subjects: {', '.join(s['Subjects'])}")
                print()

        case "3":
            sid = input("\nEnter the Student ID to update: ")
            for s in students:
                if s["ID"] == sid:
                    print("What do you want to update?")
                    print("1. Name\n2. Age\n3. Grade\n4. DOB\n5. Subjects")
                    update_choice = input("Enter choice: ")

                    match update_choice:
                        case "1":
                            s["Name"] = input("Enter new name: ")
                        case "2":
                            s["Age"] = input("Enter new age: ")
                        case "3":
                            s["Grade"] = input("Enter new grade: ")
                        case "4":
                            s["DOB"] = input("Enter new DOB (YYYY-MM-DD): ")
                        case "5":
                            s["Subjects"] = input("Enter subjects (comma-separated): ").split(",")
                        case _:
                            print("Invalid update choice.")
                    print("\nStudent updated successfully!\n")
                    break
            else:
                print("\nStudent ID not found!\n")

        case "4":
            sid = input("\nEnter the Student ID to delete: ")
            for i, s in enumerate(students):
                if s["ID"] == sid:
                    del students[i]
                    print(f"\nStudent with ID {sid} deleted successfully!\n")
                    break
            else:
                print("\nStudent ID not found!\n")

        case "5":
            all_subjects = set()
            for s in students:
                all_subjects.update(s["Subjects"])
            if all_subjects:
                print("\nSubjects Offered:", ", ".join(all_subjects))
            else:
                print("\nNo subjects available yet.\n")

        case "6":
            print("\nThank you for using Student Data Organizer. Goodbye!\n")
            break

        case _:
            print("\nInvalid choice. Please try again.\n")
