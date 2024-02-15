# test_employee_management.py
import unittest
from employee_management import Employee, EmployeeManagementSystem

class TestEmployeeManagementSystem(unittest.TestCase):
    def setUp(self):
        self.emp_sys = EmployeeManagementSystem()
        self.emp_sys.add_employee("John", 30, 1, "HR")
        self.emp_sys.add_employee("Alice", 25, 2, "IT")
        self.emp_sys.add_employee("Bob", 35, 3, "Finance")

    def test_add_employee(self):
        self.emp_sys.add_employee("Emma", 28, 4, "Marketing")
        self.assertEqual(len(self.emp_sys.employees), 4)

    def test_get_employee_by_id(self):
        emp = self.emp_sys.get_employee_by_id(2)
        self.assertEqual(emp.name, "Alice")

    def test_delete_employee_by_id(self):
        self.assertTrue(self.emp_sys.delete_employee_by_id(3))
        self.assertEqual(len(self.emp_sys.employees), 2)

if __name__ == '__main__':
    unittest.main()
