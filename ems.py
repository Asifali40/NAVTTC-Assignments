# Employee Management System (EMS) - Alternative Implementation

# Initialize an empty dictionary to store employee data
employee_data = {}

def add_employee():
    """Add a new employee to the dictionary."""
    try:
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Employee Name: ")
        position = input("Enter Employee Position: ")
        salary = input("Enter Employee Salary: ")

        # Create an employee record
        employee = {
            "Name": name,
            "Position": position,
            "Salary": salary
        }

        # Add employee to the dictionary
        employee_data[emp_id] = employee
        print("Employee added successfully!")
    except Exception as e:
        print(f"Error adding employee: {e}")

def display_employees():
    """Display all employee details from the dictionary."""
    if not employee_data:
        print("No employee data found.")
        return

    print("\nEmployee Details:")
    for emp_id, employee in employee_data.items():
        print(f"Employee ID: {emp_id}")
        print(f"Name: {employee['Name']}")
        print(f"Position: {employee['Position']}")
        print(f"Salary: {employee['Salary']}")
        print("-" * 30)

def main():
    while True:
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. Display Employees")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            add_employee()
        elif choice == "2":
            display_employees()
        elif choice == "3":
            print("Exiting the program. Have a great day!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if _name_ == "_main_":
    main()
