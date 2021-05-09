import requests

# def decorator(f):
#     """A decorator example for comprehension"""
#     def new_function():
#         print("Extra functionality")
#         f()
#     return new_function()
#
#
# @decorator
# def initial_function():
#     print("Initial functionality")
#
#
# initial_function()


class Employee:
    """A sample Employee class"""

    raise_amt = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def email(self):
        return f"{self.first}.{self.last}@email.com"

    @property
    def fullname(self):
        return f"{self.first} {self.last}".title()

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def monthly_schedule(self, month):
        response = requests.get(f"http://company.com/{self.last}/{month}")
