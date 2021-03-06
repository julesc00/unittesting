import unittest
from unittest.mock import patch

from employee import Employee


class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.emp_1 = Employee("Claudia", "Huerta", 50000)
        self.emp_2 = Employee("Julio", "Briones", 60000)

    def tearDown(self):
        """For database mocking cleanup."""
        pass

    def test_email(self):
        """Test employee email is created from fullname."""

        self.assertEqual(self.emp_1.email, "Claudia.Huerta@email.com")
        self.assertEqual(self.emp_2.email, "Julio.Briones@email.com")

        self.emp_1.first = "Caricia"
        self.emp_2.first = "Franzche"

        self.assertEqual(self.emp_1.email, "Caricia.Huerta@email.com")
        self.assertEqual(self.emp_2.email, "Franzche.Briones@email.com")

    def test_fullname(self):
        """Test employee fullname is created from first and last name."""

        self.assertEqual(self.emp_1.fullname, "Claudia Huerta")
        self.assertEqual(self.emp_2.fullname, "Julio Briones")

        self.emp_1.first = "lucien"
        self.emp_2.first = "jules"

        self.assertEqual(self.emp_1.fullname, "Lucien Huerta")
        self.assertEqual(self.emp_2.fullname, "Jules Briones")

    def test_apply_raise(self):
        """Test employee raise is applied to pay."""
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)

    def test_monthly_schedule(self):
        with patch("employee.requests.get") as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = "Success"

            schedule = self.emp_1.monthly_schedule("May")
            mocked_get.assert_called_with("http://company.com/Huerta/May")

            self.assertEqual(schedule, "Success")

            mocked_get.return_value.ok = False

            schedule = self.emp_2.monthly_schedule("June")
            mocked_get.assert_called_with("http://company.com/Briones/June")

            self.assertEqual(schedule, "Bad response!")


# To run unittest automatically when running the file.
if __name__ == "__main__":
    unittest.main()
