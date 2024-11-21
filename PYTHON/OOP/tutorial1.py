class Employee:

    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

emp_1 = Employee('Mahmudur', 'rahman' , 60000)
emp_2 = Employee('Harvy','the destroyer', 75000)

#print(emp_1.email) 
#print('{} {}'.format(emp_2.first, emp_2.last))
#print('{} {}'.format(emp_1.first, emp_1.last))
print(emp_1.pay)