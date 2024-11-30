class Employee:

    raise_amount = 1.04
    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@email.com'

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

#emp_str_1 = 'Nadim-hossain-50000'
#first, last, pay = emp_str_1.split('-')

#new_employee_1 = Employee.seperate(emp_str_1)
#print(new_employee_1.pay)

#import datetime
#my_date = datetime.date(2016, 5, 22)
#print(Employee.is_workday(my_date))

class Developer(Employee) :
    raise_amount = 3
    num_of_devs = 0

    def __init__(self, first, last, pay, programme_language):
        super().__init__(first, last, pay)
        self.programme_language = programme_language

        Developer.num_of_devs += 1

dev_1 = Developer('Mango', 'Khan', 10000, 'Python')
dev_2 = Developer('Lichi', 'Amir', 20000, 'C++')
dev_3 = Developer('Chango', 'cameleon', 30000, 'Java')

print (dev_1.email)
dev_2.apply_raise()
print (dev_2.pay)
print (dev_1.programme_language)
print (dev_3.programme_language)
print (dev_3.email)
print (Developer.num_of_devs)


class Manager(Employee):
    def __init__(self, first, last, pay, employee = None):
        super().__init__(first, last, pay)

        if employee is None:
            self.employee = []
        else:
            self.employee = employee

    def add_emp(self, emp):
        if emp not in self.employee:
            self.employee.append(emp)
    def remove_emp(self, emp):
        if emp in self.employee:
            self.employee.remove(emp)     

    def print_emp(self):
        for emp in self.employee:
            print('---> ', emp.fullname())

mgr_1 = Manager('Yemete', 'jing', 90000, [dev_2])

print(mgr_1.email)
mgr_1.add_emp(dev_1)
mgr_1.add_emp(dev_3)
mgr_1.remove_emp(dev_2)
mgr_1.print_emp()

print(isinstance(mgr_1, Developer))
print(issubclass(Developer, Employee))