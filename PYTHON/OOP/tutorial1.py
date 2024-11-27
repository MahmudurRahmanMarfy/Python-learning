class Employee:

    raise_amount = 1.04
    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def seperate(cls , emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
    
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp_1 = Employee('Mahmudur', 'rahman' , 60000)
emp_2 = Employee('Harvy','the destroyer', 75000)
emp_3 = Employee('Nadim','vokochoko', 70000)

#print(emp_1.email) 
#print('{} {}'.format(emp_2.first, emp_2.last))
#print('{} {}'.format(emp_1.first, emp_1.last))

#emp_1.raise_amount = 2
#emp_1.apply_raise()
#print(emp_1.raise_amount)
#print(emp_1.pay)
#
#print(emp_2.pay)
#emp_2.apply_raise()
#print(emp_2.raise_amount)
#print(emp_2.pay)
#
#print(Employee.num_of_emps)

#Employee.set_raise_amount(2)
#emp_2.apply_raise()
#emp_1.apply_raise()
#print(emp_1.pay)
#print(emp_2.pay)

emp_str_1 = 'Nadim-hossain-50000'
first, last, pay = emp_str_1.split('-')

new_employee_1 = Employee.seperate(emp_str_1)
print(new_employee_1.pay)

import datetime
my_date = datetime.date(2016, 5, 22)
print(Employee.is_workday(my_date))