# employee_management.py

class Employee:
    def __init__(self, name, age, emp_id, department):
        self.name = name
        self.age = age
        self.emp_id = emp_id
        self.department = department

class EmployeeManagementSystem:
    def __init__(self):
        self.employees = []

    def add_employee(self, name, age, emp_id, department):
        emp = Employee(name, age, emp_id, department)
        self.employees.append(emp)

    def get_employee_by_id(self, emp_id):
        for emp in self.employees:
            if emp.emp_id == emp_id:
                return emp
        return None

    def delete_employee_by_id(self, emp_id):
        for emp in self.employees:
            if emp.emp_id == emp_id:
                self.employees.remove(emp)
                return True
        return False
