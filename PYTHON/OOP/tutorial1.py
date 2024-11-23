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

emp_1 = Employee('Mahmudur', 'rahman' , 60000)
emp_2 = Employee('Harvy','the destroyer', 75000)
emp_3 = Employee('Nadim','vokochoko', 70000)

#print(emp_1.email) 
#print('{} {}'.format(emp_2.first, emp_2.last))
#print('{} {}'.format(emp_1.first, emp_1.last))

emp_1.raise_amount = 2
emp_1.apply_raise()
print(emp_1.raise_amount)
print(emp_1.pay)

print(emp_2.pay)
emp_2.apply_raise()
print(emp_2.raise_amount)
print(emp_2.pay)

print(Employee.num_of_emps)