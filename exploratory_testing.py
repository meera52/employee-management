from employee_management import EmployeeManagementSystem
emp_sys = EmployeeManagementSystem()

# Add employees
emp_sys.add_employee("John", 30, 1, "HR")
emp_sys.add_employee("Alice", 25, 2, "IT")

# Retrieve employee information
john = emp_sys.get_employee_by_id(1)
print(john.name)  # Output: "John"

# Delete an employee
emp_sys.delete_employee_by_id(2)
