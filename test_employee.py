import unittest

from employee import Employee


class TestEmployee(unittest.TestCase):

    def test_email(self):
        """Test employee email is created from fullname."""
        emp_1 = Employee("Benito", "Briones", 20000)
        emp_2 = Employee("Charbelito", "Briones", 22000)

        self.assertEqual(emp_1.email, "Benito.Briones@email.com")
        self.assertEqual(emp_2.email, "Charbelito.Briones@email.com")

        emp_1.first = "Caricia"
        emp_2.first = "Franzche"

        self.assertEqual(emp_1.email, "Caricia.Briones@email.com")
        self.assertEqual(emp_2.email, "Franzche.Briones@email.com")

    def test_fullname(self):
        """Test employee fullname is created from first and last name."""
        emp_1 = Employee("benito", "briones", 50000)
        emp_2 = Employee("brigitte", "briones", 60000)

        self.assertEqual(emp_1.fullname, "Benito Briones")
        self.assertEqual(emp_2.fullname, "Brigitte Briones")

        emp_1.first = "lucien"
        emp_2.first = "jules"

        self.assertEqual(emp_1.fullname, "Lucien Briones")
        self.assertEqual(emp_2.fullname, "Jules Briones")

    def test_apply_raise(self):
        """Test employee raise is applied to pay."""
        emp_1 = Employee("Claudia", "Huerta", 50000)
        emp_2 = Employee("Julio", "Briones", 60000)

        emp_1.apply_raise()
        emp_2.apply_raise()

        self.assertEqual(emp_1.pay, 52500)
        self.assertEqual(emp_2.pay, 63000)


# To run unittest automatically when running the file.
if __name__ == "__main__":
    unittest.main()
