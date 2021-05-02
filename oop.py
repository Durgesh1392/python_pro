# python object oriented programming

class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)  # return self.first + ' '+ self.last


emp_1 = Employee('durgesh', 'kumar', 90000)
emp_2 = Employee('vijay', 'prakash', 80000)

# print(emp_1.first)
# print(emp_2.email)
print(emp_1.fullname())
print(Employee.fullname(emp_1))
