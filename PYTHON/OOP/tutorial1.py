class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('Mahmudur', 'rahman' , 60000)
emp_2 = Employee('Harvy','the destroyer', 75000)

print(emp_1.email) 
print(emp_2.pay)

#print('{} {}'.format(emp_2.first, emp_2.last))
#print('{} {}'.format(emp_1.first, emp_1.last))

print(emp_1.fullname())
print(Employee.fullname(emp_2))