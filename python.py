# Import necessary modules
import student_management_system as sms  # Import module for student management system

def display_menu():
    """Display the main menu."""
    print("Student Management System")
    print("1. Add Student")
    print("2. Remove Student")
    print("3. View All Students")
    print("4. View Specific Student")
    print("5. Exit")

def main():
    # Initialize the student management system
    sms.initialize()

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            sms.add_student()
        elif choice == "2":
            sms.remove_student()
        elif choice == "3":
            sms.view_all_students()
        elif choice == "4":
            sms.view_specific_student()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
